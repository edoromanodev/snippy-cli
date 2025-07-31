import json
import os

FILENAME = "snip.json"


def load_snippets():
    with open(FILENAME, "r") as f:
        return json.load(f)


def save_snippets(snippets):
    with open(FILENAME, "w") as f:
        json.dump(snippets, f, indent=4)


def run(args):
    """
    Rimuove uno snippet:
      remove <name>
    """

    if len(args) != 1:
        print("Error: Correct usage -> remove <name> ")
        return

    name_to_remove = args[0]
    snippets = load_snippets()

    new_snippets = [s for s in snippets if s["name"] != name_to_remove]

    if len(new_snippets) == len(snippets):
        print(f"Nessuno snippet trovato con il nome '{name_to_remove}'.")
        return

    save_snippets(new_snippets)
    print(f"✅ Snippet '{name_to_remove}' rimosso con successo.")
