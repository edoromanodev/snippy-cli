def parse(command: str) -> tuple[str, list[str]]:
    parts = command.strip().split()
    if not parts:
        raise ValueError("Bad request :(")
    cmd_name = parts[0]
    args = parts[1:]
    return cmd_name, args
