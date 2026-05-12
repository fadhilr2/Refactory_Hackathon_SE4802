## ADDED Requirements

### Requirement: Typer CLI App Structure
The system SHALL use Typer to create a command-line interface application in the `cli/main.py` file.

#### Scenario: User invokes help command
- **WHEN** user runs the CLI with the `--help` flag
- **THEN** system displays the available commands (init, reset) and their descriptions

### Requirement: Exception Handling
The system SHALL handle all potential user input exceptions and provide actionable feedback messages without crashing.

#### Scenario: Exception occurs during user input
- **WHEN** user provides invalid input or interrupts the prompt
- **THEN** system catches the exception and prints a descriptive error message with suggested actions
