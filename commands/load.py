import subprocess
import platform
import json
import os

FILENAME = "snip.json"
os_name = platform.system()

def load_snippets():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)

def copy(code):
    try:
        if os_name == "Windows":
            subprocess.run("clip", text=True, input=code)
        elif os_name == "Darwin":
            subprocess.run("pbcopy", text=True, input=code)
        elif os_name == "Linux":
          
            p = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
            p.communicate(input=code.encode('utf-8'))
        else:
            print(f"❌ Sistema operativo sconosciuto: {os_name}")
            return
        print("✅ Codice copiato negli appunti.")
    except Exception as e:
        print(f"❌ Errore nella copia: {e}")

def run(args):
    """ 
    Copia uno snippet:
      load <name>
    """
    if len(args) != 1:
        print("Error: Correct usage -> load <name>")
        return

    snippets = load_snippets()
    name_to_load = args[0]

    snippet = next((s for s in snippets if s["name"] == name_to_load), None)

    if snippet is None:
        print(f"❌ Nessuno snippet trovato con il nome '{name_to_load}'.")
        return

    copy(snippet["code"])
