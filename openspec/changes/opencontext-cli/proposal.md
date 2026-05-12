## Why

We need to create a command-line interface (CLI) application named OpenContext to handle project initialization and agent file generation. This will simplify the setup process for users by interactively requesting configuration data and automatically generating required project files, reducing manual configuration errors and standardizing the setup workflow.

## What Changes

- Set up a new Python project in the `cli` directory using `typer` for routing and `questionary` for interactive prompts.
- Implement an `init` command that interactively populates a `opencontext.config.json` file with `OPENCONTEXT_IS_INIT`, `JIRA_LINK`, and `PROJECT_DIRECTORY`.
- Implement a `reset` command that reverts `opencontext.config.json` to its default, pre-initialized state.
- Create a `utils.py` module to handle configuration file reading/writing and the generation of an `agent.md` file.
- Add an internal method called during initialization to process mock markdown data and generate `agent.md`.
- Add robust exception handling and user feedback for all CLI interactions.

## Capabilities

### New Capabilities
- `cli-core`: The base Typer application setup, routing, exception handling, and user feedback.
- `cli-configuration`: Interactive configuration management reading/writing `opencontext.config.json` using `questionary`.
- `agent-generation`: Internal functionality to process markdown data and generate the `agent.md` execution file.

### Modified Capabilities
- (None)

## Impact

- Introduces a new `cli` folder containing the Python application.
- Adds new Python dependencies: `typer` and `questionary`.
- Generates `opencontext.config.json` and `agent.md` in the working directory based on user interactions.
