## Context

The system needs to store unstructured string data and make it searchable via embeddings. We are standardizing on LanceDB for local vector storage, specifically targeting the `.sdlc/dataVektor` directory. We need a core function within the `pipeline` module to handle the ingestion of raw strings.

## Goals / Non-Goals

**Goals:**
- Provide a clear API for string vectorization.
- Generate embeddings from a string parameter.
- Save the embeddings with the original string (as context) into LanceDB at `.sdlc/dataVektor`.

**Non-Goals:**
- Handling chunking of extremely large strings (for now, assume the string is appropriately sized or chunking happens upstream).
- Extracting text from files like PDF or Jira (handled in other pipelines).

## Decisions

- **Embedding Model**: Use the existing default embedding model to convert the string to a vector.
- **Database Schema**: Define a Pydantic model for LanceDB that includes at minimum `text` (string) and `vector` (list of floats).
- **Function Signature**: `def process_string_to_vector(text: str) -> bool:` (returning success status). The function should create the table if it doesn't exist.
- **LanceDB connection**: Connect to LanceDB using the local URI `lancedb.connect(".sdlc/dataVektor")`.

## Risks / Trade-offs

- **Risk: Embedding Dimension Mismatch**: If the table already exists, the incoming vector dimensions must match the schema.
  - *Mitigation*: Ensure the embedding model used is consistent and the schema explicitly specifies the dimension if possible, or gracefully handles table creation/appending.
- **Risk: Duplicate Entries**: Re-running the pipeline might duplicate the string vector.
  - *Mitigation*: Depending on the use case, we either accept duplicates or generate a unique ID based on a hash of the string text.
