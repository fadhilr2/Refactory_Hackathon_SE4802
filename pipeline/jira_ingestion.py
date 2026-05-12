from __future__ import annotations
import os
import json
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry

# Initialize the embedder
embedder = get_registry().get("sentence-transformers").create(name="all-MiniLM-L6-v2", device="cpu")

# Create a type alias for the vector field to satisfy linters
JiraVector = Vector(embedder.ndims())

# Define the schema using Pydantic
class JiraTicket(LanceModel):
    key: str
    text: str = embedder.SourceField()
    vector: JiraVector = embedder.VectorField()

def ensure_directory(path: str):
    """Ensure the directory exists."""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def parse_adf(content: list) -> str:
    """Recursively parse Atlassian Document Format (ADF) content to extract plain text."""
    extracted = []
    if not isinstance(content, list):
        return ""
    for item in content:
        if isinstance(item, dict):
            if item.get("type") == "text":
                extracted.append(item.get("text", ""))
            elif "content" in item:
                extracted.append(parse_adf(item["content"]))
    return " ".join(extracted).strip()

def process_jira_ticket(ticket_json: dict) -> dict:
    """Extract and concatenate required fields from the Jira ticket JSON."""
    key = ticket_json.get("key", "")
    fields = ticket_json.get("fields", {})
    
    summary = fields.get("summary", "")
    
    # Process labels
    labels_list = fields.get("labels", [])
    labels = " ".join(labels_list) if labels_list else ""
    
    # Process components
    components_list = fields.get("components", [])
    components = " ".join([c.get("name", "") for c in components_list]) if components_list else ""
    
    # Process description
    description_obj = fields.get("description", {})
    description_text = ""
    if description_obj and isinstance(description_obj, dict):
        if description_obj.get("type") == "doc":
            description_text = parse_adf(description_obj.get("content", []))
        elif isinstance(description_obj, str):
            description_text = description_obj
    elif isinstance(description_obj, str):
        description_text = description_obj
            
    # Process comments
    comment_data = fields.get("comment", {})
    # Sometimes it's nested under fields.comment.comments
    comments_obj = comment_data.get("comments", []) if isinstance(comment_data, dict) else []
    
    comments_text_list = []
    for comment in comments_obj:
        author = comment.get("author", {}).get("displayName", "Unknown")
        body_obj = comment.get("body", {})
        body_text = ""
        if isinstance(body_obj, dict) and body_obj.get("type") == "doc":
            body_text = parse_adf(body_obj.get("content", []))
        elif isinstance(body_obj, str):
            body_text = body_obj
        comments_text_list.append(f"{author}: {body_text}")
        
    comments_text = " | ".join(comments_text_list)
    
    # Concatenate all fields
    full_text = f"Summary: {summary}\nLabels: {labels}\nComponents: {components}\nDescription: {description_text}\nComments: {comments_text}"
    
    return {
        "key": key,
        "text": full_text
    }

def ingest_ticket(ticket_json: dict, db_path: str = ".sdlc/dataVector", table_name: str = "jira_tickets"):
    """Ingest a single Jira ticket JSON into LanceDB."""
    ensure_directory(db_path)
    
    print(f"Connecting to LanceDB at {db_path}...")
    db = lancedb.connect(db_path)
    
    if table_name in db.table_names():
        table = db.open_table(table_name)
    else:
        print(f"Creating table '{table_name}'...")
        table = db.create_table(table_name, schema=JiraTicket)
        
    processed_data = process_jira_ticket(ticket_json)
    print(f"Extracted context string for {processed_data['key']} length: {len(processed_data['text'])}")
    
    # Insert data
    print(f"Vectorizing and storing ticket {processed_data['key']}...")
    table.add([processed_data])
    print("Done!")
    return processed_data

if __name__ == "__main__":
    # Test payload to verify the ingestion
    sample_ticket = {
        "key": "KAN-123",
        "fields": {
            "summary": "Fix login button styling",
            "labels": ["frontend", "bug"],
            "components": [{"name": "UI"}],
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {"type": "text", "text": "The login button is misaligned on mobile devices."}
                        ]
                    }
                ]
            },
            "comment": {
                "comments": [
                    {
                        "author": {"displayName": "John Doe"},
                        "body": {
                            "type": "doc",
                            "version": 1,
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {"type": "text", "text": "I can reproduce this on iOS Safari."}
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
    
    ingest_ticket(sample_ticket)
