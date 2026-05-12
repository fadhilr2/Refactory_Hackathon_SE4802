## Why

OpenContext requires a clear, flat, and purpose-driven directory structure to serve as an automated Staff Engineer CLI tool. A local-first, git-hook-driven setup ensures data privacy, quick context extraction without relying on external services, and straightforward integration into existing development workflows.

## What Changes

- Create a flat root directory structure with exactly three main folders: `cli/`, `pipeline/`, and `inference/`. No subdirectories should be created initially.
- The `cli/` directory will serve as the entry point and interface for all user commands.
- The `pipeline/` directory will handle data ingestion, extracting context from SRS/SDD documents (.pdf, .docx, .md, .txt), fetching Jira ticket details via regex, and tracking git diffs.
- The `inference/` directory will manage 100% local AI processing using Ollama to handle embedding generation and synthesize context into `agents.md`.

## Capabilities

### New Capabilities
- `directory-structure`: Establishing the core repository layout and organizing the distinct components (CLI, data pipeline, and local AI inference) into a strict flat structure.

### Modified Capabilities

## Impact

- Sets the foundational layout for the OpenContext repository, ensuring separation of concerns among the CLI layer, data ingestion pipeline, and local AI inference engine.
- Defines boundaries that future components and implementations must respect (e.g., maintaining a flat structure and local-first operations).
