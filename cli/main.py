import sys
import os

# Add the project root directory to sys.path so modules like 'fetcher' and 'cli' can be found
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import typer
import questionary
from cli.utils import get_config, save_config, reset_config, generate_agent_file, get_branch_ticket
from fetcher.jira_retriever import fetch_jira_ticket
from fetcher.spec_fetcher import fetch_spec
from pipeline.string_vectorizer import process_string_to_vector

app = typer.Typer(help="OpenContext CLI for agent generation and configuration")

@app.command()
def tes():
    print("tes")

@app.command()
def init():
    try:
        config = get_config()
        
        # Interactive prompts using questionary
        jira_domain = questionary.text(
            "Enter JIRA Domain:",
            default=config.get("JIRA_DOMAIN", "")
        ).ask()
        if jira_domain is None: raise KeyboardInterrupt
        
        jira_api_key = questionary.password(
            "Enter JIRA API Key:"
        ).ask()
        if jira_api_key is None: raise KeyboardInterrupt
        
        jira_email = questionary.text(
            "Enter JIRA Email:",
            default=config.get("JIRA_EMAIL", "")
        ).ask()
        if jira_email is None: raise KeyboardInterrupt
        
        ai_model = questionary.select(
            "Enter AI Model:",
            choices=[
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-2.5-pro",
            ],
        ).ask()
        if ai_model is None: raise KeyboardInterrupt
        
        ai_api_key = questionary.password(
            "Enter AI API Key:"
        ).ask()
        if ai_api_key is None: raise KeyboardInterrupt
             
        import os
        project_directory = os.getcwd()
            
        config["OPENCONTEXT_IS_INIT"] = 1
        config["PROJECT_DIRECTORY"] = project_directory
        config["JIRA_DOMAIN"] = jira_domain
        config["JIRA_API_KEY"] = jira_api_key
        config["JIRA_EMAIL"] = jira_email
        config["AI_MODEL"] = ai_model
        config["AI_API_KEY"] = ai_api_key
        config["JIRA_TICKET"] = get_branch_ticket()
        
        spec_stringify = fetch_spec(config["AI_API_KEY"], config["AI_MODEL"])
        is_save_to_vector_success = process_string_to_vector(spec_stringify)

        if(is_save_to_vector_success):
            print("Specification has been vectorized successfully.")

        jira_data = fetch_jira_ticket(config["JIRA_DOMAIN"], config["JIRA_API_KEY"], config["JIRA_EMAIL"], config["JIRA_TICKET"])
        
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
