import os
import json
from pathlib import Path

CONFIG_FILE = "opencontext.config.json"
DEFAULT_CONFIG = {
    "OPENCONTEXT_IS_INIT": 0,
    "JIRA_LINK": "",
    "PROJECT_DIRECTORY": ""
}

def get_config() -> dict:
    try:
        config_path = Path(CONFIG_FILE)
        if config_path.exists():
            with open(config_path, "r") as f:
                return json.load(f)
        return DEFAULT_CONFIG.copy()
    except Exception as e:
        print(f"Error reading config: {e}")
        return DEFAULT_CONFIG.copy()

def save_config(config: dict):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Error saving config: {e}. Please check your permissions.")

def reset_config():
    save_config(DEFAULT_CONFIG)

def generate_agent_file(markdown_data: str):
    try:
        with open("agent.md", "w") as f:
            f.write(markdown_data)
        print("Successfully generated agent.md")
    except Exception as e:
        print(f"Error generating agent.md: {e}. Please check your permissions.")
