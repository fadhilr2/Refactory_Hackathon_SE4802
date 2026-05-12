## 1. Project Setup

- [x] 1.1 Create `cli` folder and essential files (`main.py`, `utils.py`)
- [x] 1.2 Add `typer` and `questionary` to the environment (or generate a `requirements.txt`)

## 2. Utilities Implementation

- [x] 2.1 Implement `get_config()` and `save_config()` in `cli/utils.py` to read/write `opencontext.config.json`
- [x] 2.2 Implement `reset_config()` in `cli/utils.py` to restore defaults (`OPENCONTEXT_IS_INIT`=0, `JIRA_LINK`="", `PROJECT_DIRECTORY`="")
- [x] 2.3 Implement `generate_agent_file(markdown_data: str)` in `cli/utils.py` to create `agent.md` with the provided string

## 3. CLI Core & Commands

- [x] 3.1 Initialize the Typer app in `cli/main.py`
- [x] 3.2 Implement `init` command using `questionary` to prompt for `OPENCONTEXT_IS_INIT`, `JIRA_LINK`, and `PROJECT_DIRECTORY`
- [x] 3.3 Inside the `init` command, pass mock markdown data to `generate_agent_file()` from `utils.py`
- [x] 3.4 Implement `reset` command calling `reset_config()`
- [x] 3.5 Add success messages ("OpenSpec has been initialized successfully", etc.)

## 4. Exception Handling & Polish

- [x] 4.1 Wrap file I/O operations in try-except blocks and provide actionable error messages
- [x] 4.2 Catch `KeyboardInterrupt` / Typer aborts gracefully during interactive prompts
