## Why

To support advanced search or AI features, we need a way to vectorize raw strings and store them in a local vector database. By converting text to embeddings and storing it in LanceDB, we enable scalable similarity search over textual data.

## What Changes

- Create a new string vectorization module/function in the `pipeline` directory.
- The function will take a raw string, generate vector embeddings, and save the resulting data into LanceDB.
- Set the LanceDB storage path to `.sdlc/dataVektor`.

## Capabilities

### New Capabilities
- `string-vectorization`: A function that accepts a string, performs embedded vectorization, and stores it in the local LanceDB instance at `.sdlc/dataVektor`.

### Modified Capabilities

## Impact

- Adds new functionality to the `pipeline` folder.
- Creates/uses a LanceDB instance at `.sdlc/dataVektor`.
- Introduces dependencies on LanceDB and the existing embedding model/library used in the project.
