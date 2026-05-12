## Context

We need a CLI tool named OpenContext. The goal is to set up some configuration parameters (like `OPENCONTEXT_IS_INIT`, `JIRA_LINK`, `PROJECT_DIRECTORY`) in a `opencontext.config.json` file. The CLI should interactively prompt the user for these details, using `typer` and `questionary`. For `PROJECT_DIRECTORY` in `opencontext.config.json` use the current working directory where the init command is invoked. Additionally, the CLI needs a method to generate an `agent.md` file from markdown data coming from an `inference` folder (which will be mocked for now).

## Goals / Non-Goals

**Goals:**
- Implement the CLI tool using `typer` and `questionary`.
- Create clean and descriptive code in the `CLI` directory.
- Allow users to initialize and reset the configuration.
- Handle user input exceptions gracefully with actionable feedback.
- Produce `opencontext.config.json` and `agent.md` files locally.

**Non-Goals:**
- Implement the actual inference folder structure or logic in this phase (using mock data instead).
- Make modifications to any folder other than the `CLI` folder.

## Decisions

- **CLI Framework:** Use `typer` for building the CLI because of its intuitive interface and support for type hints.
- **Interactive Prompts:** Use `questionary` for robust interactive user prompts when collecting the initialization data.
- **Data Storage:** Store the settings locally in `opencontext.config.json` within the current working directory to allow per-project configurations.
- **Project Structure:** Place all Python files in a `cli` module (`cli/main.py`, `cli/utils.py`) to keep everything isolated as requested.
- **Exception Handling:** Wrap file operations (reading/writing `opencontext.config.json` and `agent.md`) in try-except blocks. When an error occurs, print a clear, colorized message to the console advising the user on how to fix it instead of crashing.

## Risks / Trade-offs

- **Risk:** The working directory might lack write permissions, causing the creation of `opencontext.config.json` or `agent.md` to fail.
  - **Mitigation:** Wrap file creation inside `try/except` and provide an actionable error message suggesting the user to check directory permissions.
- **Risk:** User aborts interactive prompts (e.g., hitting Ctrl+C).
  - **Mitigation:** Catch `KeyboardInterrupt` or similar exceptions from `questionary` and exit cleanly without generating a stack trace.
