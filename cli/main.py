import sys
import typer
import questionary
from utils import get_config, save_config, reset_config, generate_agent_file

app = typer.Typer(help="OpenContext CLI for agent generation and configuration")

@app.command()
def init():
    try:
        config = get_config()
        
        # Interactive prompts using questionary
        jira_link = questionary.text(
            "Enter JIRA Link:",
            default=config.get("JIRA_LINK", "")
        ).ask()
        
        if jira_link is None:
            raise KeyboardInterrupt
             
        import os
        project_directory = os.getcwd()
            
        config["OPENCONTEXT_IS_INIT"] = 1
        config["JIRA_LINK"] = jira_link
        config["PROJECT_DIRECTORY"] = project_directory
        
        save_config(config)
        typer.echo("OpenSpec has been initialized successfully.")
        
        # Internal method to generate agent.md with mock data
        mock_markdown = "# Agent\nThis is a mock agent markdown file generated from inference."
        generate_agent_file(mock_markdown)
        
    except KeyboardInterrupt:
        typer.echo("\nInitialization aborted by user. Please run `python -m cli.main init` to try again.", err=True)
        sys.exit(1)
    except Exception as e:
        typer.echo(f"An unexpected error occurred during initialization: {e}", err=True)
        sys.exit(1)

@app.command()
def reset():
    try:
        reset_config()
        typer.echo("Configuration has been reset to defaults successfully.")
    except Exception as e:
        typer.echo(f"An unexpected error occurred during reset: {e}", err=True)
        sys.exit(1)

if __name__ == "__main__":
    app()
