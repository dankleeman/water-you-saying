import time
from pathlib import Path

import typer

from app import image, keyboard, llm

PROMPT_DIR_PATH = Path('prompts')

def get_prompt(prompt_file: str | None = None):
    if prompt_file:
        with open(PROMPT_DIR_PATH / prompt_file) as f:
            prompt = f.read().strip()
        return prompt
    return None

def main(user_prompt_file: str | None = None, system_prompt_file: str | None = None, use_vision: bool = False):
    user_prompt = get_prompt(user_prompt_file)
    system_prompt = get_prompt(system_prompt_file)

    while True:
        keyboard.wait_until_shortcut()

        enc_image_str = None
        if use_vision:
            screenshot = image.take_screenshot(save_filename='image.png')
            enc_image_str = image.encode_image(screenshot)

        response = llm.get_open_ai_response(user_prompt, system_prompt, enc_image_str=enc_image_str)
        print(response)
        keyboard.output(response)
        time.sleep(0.1)


if __name__ == "__main__":
    typer.run(main)
