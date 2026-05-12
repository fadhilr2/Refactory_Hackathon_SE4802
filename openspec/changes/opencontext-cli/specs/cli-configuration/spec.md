## ADDED Requirements

### Requirement: Initialize Configuration
The system SHALL provide an `init` command that interactively collects configuration values (`OPENCONTEXT_IS_INIT`, `JIRA_LINK`, `PROJECT_DIRECTORY`) using `questionary` and saves them to `opencontext.config.json`. The `PROJECT_DIRECTORY` in `opencontext.config.json` SHALL be the current working directory where the `init` command is invoked.

#### Scenario: Successful initialization
- **WHEN** user runs the `init` command and provides valid responses
- **THEN** system generates or updates `opencontext.config.json` with the provided data and displays a success message "OpenSpec has been initialized successfully"

### Requirement: Reset Configuration
The system SHALL provide a `reset` command that reverts `opencontext.config.json` to its default state.

#### Scenario: Successful reset
- **WHEN** user runs the `reset` command
- **THEN** system overwrites `opencontext.config.json` with default values and displays a success message
