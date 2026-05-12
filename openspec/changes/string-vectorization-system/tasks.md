## 1. Setup Data Models and Schema

- [x] 1.1 Create/verify the Pydantic schema for string embedding (e.g., `StringChunk` with `text` and `vector` fields).
- [x] 1.2 Ensure the LanceDB connection points to `.sdlc/dataVektor`.

## 2. Core Implementation

- [x] 2.1 Implement `process_string_to_vector` function in the `pipeline` module.
- [x] 2.2 Integrate the existing embedding model to generate vectors from the input string.
- [x] 2.3 Implement LanceDB table creation/insertion logic for the generated vectors.
- [x] 2.4 Add error handling and logging to ensure the function returns success/failure cleanly.
