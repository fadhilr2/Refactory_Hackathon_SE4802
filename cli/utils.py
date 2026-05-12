import os
import json
import subprocess
from pathlib import Path

CONFIG_FILE = "opencontext.config.json"
DEFAULT_CONFIG = {
    "OPENCONTEXT_IS_INIT": 0,
    "PROJECT_DIRECTORY": "",
    "JIRA_DOMAIN": "",
    "JIRA_API_KEY": "",
    "JIRA_EMAIL": "",
    "AI_MODEL": "",
    "AI_API_KEY": "",
    "JIRA_TICKET": ""
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

def get_branch_ticket() -> str:
    try:
        branch = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True
        )

        branchStrip = branch.stdout.strip()

        if(branchStrip == "main"):
            return branchStrip

        result = "-".join(branchStrip.split("-")[:2]) 
        return result
    except Exception as e:
        print(f"Error getting git branch: {e}")
        return ""

# def setup_post_checkout_hook():
#     hook_path = Path(".git/hooks/post-checkout")
#     hook_command = """
# # OpenContext automatic JIRA_TICKET update
# python -c "import sys, os; sys.path.append(os.getcwd()); from cli.utils import get_config, save_config, get_branch_ticket; config=get_config(); config['JIRA_TICKET']=get_branch_ticket(); save_config(config)"
# """
#     try:
#         if hook_path.exists():
#             if os.path.getsize(hook_path) == 0:
#                 with open(hook_path, "w") as f:
#                     f.write("#!/bin/sh" + hook_command)
#             else:
#                 # Append if not empty
#                 with open(hook_path, "a") as f:
#                     f.write(hook_command)
#         else:
#             if hook_path.parent.exists():
#                 with open(hook_path, "w") as f:
#                     f.write("#!/bin/sh" + hook_command)
                
#                 import stat
#                 st = os.stat(hook_path)
#                 os.chmod(hook_path, st.st_mode | stat.S_IEXEC | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
#     except Exception as e:
#         print(f"Error setting up post-checkout hook: {e}")
