import json
import os

FILENAME = "snip.json"


if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        json.dump([], f, indent=4)  
    print(f"File created: '{FILENAME}'")



def load_snippets():
    with open(FILENAME, "r") as f:
        return json.load(f)


def save_snippets(snippets):
    with open(FILENAME, "w") as f:
        json.dump(snippets, f, indent=4)


def read_multiline_input(prompt="Enter the code (end with a blank line):"):
    print(prompt)
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break  
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)


def run(args):
    """
    Aggiunge uno snippet:
      add <name> <language> <tags>
    poi inserisci il codice multilinea a parte.
    """

    if len(args) < 3:
        print("Error: Correct usage -> add <name> <language> <tags>")
        return

    name = args[0]
    language = args[1]
    tags = args[2]

    snippets = load_snippets()

    if any(s['name'] == name for s in snippets):
        print(f"Error: A snippet with the name already exists'{name}'.")
        return

    code = read_multiline_input()

    new_snippet = {
        "id": len(snippets) + 1,
        "name": name,
        "language": language,
        "tag": tags,
        "code": code,
        "description": ""
    }

    snippets.append(new_snippet)
    save_snippets(snippets)
    print(f"✅ Snippet '{name}' successfully added.")
