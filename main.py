# main.py
import importlib
from parser import parse  


def check_interruption(command: str) -> bool:
    """
    Check if the command is 'exit' (ignoring spaces and capitalization).
    """
    return command.strip().lower() == "exit"


def handle_command(command: str) -> None:
    """
    Analyzes and manages user command.
    """
    try:
        cmd_name, args = parse(command)
        module = importlib.import_module(f"commands.{cmd_name}")
        module.run(args)
        
    except ValueError as e:
        print(f"Parsing Error: {e}")
    except Exception as e:
        print(f"General Error: {e}")


def main() -> None:
    while True:
        user_input = input("webshell >>> ").strip()

        if not user_input:
            # Ignora input vuoto senza chiamare il parser
            continue

        if check_interruption(user_input):
            print("webshell >>> bye!")
            break

        handle_command(user_input)


if __name__ == "__main__":
    main()
