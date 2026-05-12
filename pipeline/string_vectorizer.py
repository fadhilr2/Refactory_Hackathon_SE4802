import os
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry

# Setup the embedding model from LanceDB registry
embedder = get_registry().get("sentence-transformers").create(name="all-MiniLM-L6-v2")

class StringChunk(LanceModel):
    text: str = embedder.SourceField()
    vector: Vector(384) = embedder.VectorField() # type: ignore
    
DB_PATH = ".sdlc/dataVektor"

def get_db():
    os.makedirs(DB_PATH, exist_ok=True)
    return lancedb.connect(DB_PATH)

def process_string_to_vector(text: str) -> bool:
    """
    Takes a string, performs embedded vectorization, and saves it to LanceDB.
    Returns True if successful, False otherwise.
    """
    if not text or not isinstance(text, str):
        return False
        
    try:
        db = get_db()
        table_name = "string_vectors"
        
        data = [{"text": text}]
        
        # Get or create table
        if table_name in db.table_names():
            table = db.open_table(table_name)
            table.add(data)
        else:
            table = db.create_table(table_name, schema=StringChunk)
            table.add(data)
            
        return True
    except Exception as e:
        print(f"Error vectorizing string: {e}")
        return False
