import time

from app import keyboard, llms
import typer
from pathlib import Path

PROMPT_DIR_PATH = Path('prompts')

def get_prompt(prompt_file: str | None = None):
    if prompt_file:
        with open(PROMPT_DIR_PATH / prompt_file) as f:
            prompt = f.read().strip()
        return prompt
    return None

def main(user_prompt_file: str | None = None, system_prompt_file: str | None = None):
    user_prompt = get_prompt(user_prompt_file)
    system_prompt = get_prompt(system_prompt_file)

    while True:
        keyboard.wait_until_shortcut()
        response = llms.get_open_ai_response(user_prompt, system_prompt)
        print(response)
        keyboard.output(response)
        time.sleep(0.1)


if __name__ == "__main__":
    typer.run(main)
