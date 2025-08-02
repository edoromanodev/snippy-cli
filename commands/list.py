import json
import os

FILENAME = "snip.json"

def load_snippets():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
        
    except:
        print("error")


def save_snippets(snippets):
    with open(FILENAME, "w") as f:
        json.dump(snippets, f, indent=4)


def run(args):

    if len(args) != 0:
        print("Error: Correct usage -> list")
        return

    snippets = load_snippets()

    for s in snippets:

        print("- [ID -",s['id'],"]", "name:", s['name'], "/// language:", s['language'],  "/// tag:", s['tag'])
        

    

    