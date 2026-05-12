## Context

OpenContext is being designed as an automated Staff Engineer CLI tool that runs locally and relies heavily on git hooks to track and update context. To keep the project easily navigable and modular, we are setting up the initial repository structure.

## Goals / Non-Goals

**Goals:**
- Create a flat directory structure in the root of the repository.
- Establish `cli/` for the command-line interface.
- Establish `pipeline/` for data ingestion from various document formats (PDF, DOCX, MD, TXT), Jira ticket extraction, and git diff tracking.
- Establish `inference/` for 100% local AI processing via Ollama, including embedding generation and context synthesis into `agents.md`.

**Non-Goals:**
- Implementing the actual code or tools for CLI, pipeline, or inference.
- Creating subdirectories within the main folders.

## Decisions

- **Flat directory structure**: We will avoid deep nesting from the outset to make the project approachable and keep import paths simple.
- **Top-level domain separation**: The three core domains (user interaction via CLI, context gathering via pipeline, and synthesis via inference) are isolated into their own root-level directories. This enforces clear boundaries and makes it easier to assign ownership or split into separate packages if needed later.

## Risks / Trade-offs

- [Risk] Flat structure might become cluttered. → Mitigation: We enforce strict guidelines on what belongs in `cli/`, `pipeline/`, and `inference/`. As the project grows, we may allow subdirectories within these three domains, but the root structure must remain flat.
