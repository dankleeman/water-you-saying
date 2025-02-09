import time
import typer
import sys
from app import keyboard, llms

def main():
    while True:
        keyboard.wait_until_shortcut()
        response = llms.get_open_ai_response()
        print(response)
        keyboard.output(response)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
