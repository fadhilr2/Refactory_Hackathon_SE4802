from pathlib import Path
import google.generativeai as genai
import json

def get_all_specs_markdown(target_directory="openspec/specs"):
    """
    Reads all .md files in the target directory and its subfolders,
    returning their combined content as a single string.
    """
    dir_path = Path(target_directory)
    
    # Check if the directory exists to avoid errors
    if not dir_path.exists() or not dir_path.is_dir():
        return f"Error: The directory '{target_directory}' does not exist."

    combined_markdown = []
    
    # rglob("*.md") recursively searches for all files ending in .md
    for file_path in dir_path.rglob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # Add a header for readability (optional)
                combined_markdown.append(f"\n")
                
                # Append the file content
                combined_markdown.append(file.read())
                
                # Add a footer and spacing (optional)
                combined_markdown.append(f"\n\n\n")
        except Exception as e:
            print(f"Failed to read {file_path}: {e}")

    # Join all elements in the list into a single string
    return "".join(combined_markdown)

def fetch_spec(APITOKEN: str, model_name: str = "gemini-2.5-flash"):
    data = get_all_specs_markdown()

    genai.configure(api_key=APITOKEN)

    SYSTEM_PROMPT = '''
    You are an expert software architect. Review the following software specification data and extract a comprehensive list of all architectural facts. 

    For the context of this task, an "architectural fact" includes:
    - System boundaries, core components, and their specific responsibilities.
    - Technology stack choices (languages, frameworks, databases, infrastructure).
    - Data models, storage mechanisms, and data flow paths.
    - APIs, external integrations, and communication protocols.
    - Non-functional constraints (security requirements, performance, scalability).
    - Established design patterns or architectural styles (e.g., microservices, monolith, event-driven).

    OUTPUT FORMAT:
    Return the extracted facts STRICTLY as a valid JSON array of strings. 
    Each string must be a single, distinct architectural fact. 
    Do not include any introductory or concluding text, and do not wrap the output in markdown code blocks (e.g., no ```json). Return ONLY the raw JSON array.
    '''
    try:
        model = genai.GenerativeModel(
            model_name=model_name, 
            system_instruction=SYSTEM_PROMPT,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=list[str] 
            )
        )
        response = model.generate_content(data)
        return json.loads(response.text) 
    except Exception as e:
        return f"Error: Could not initialize model '{model_name}'. {e}"

