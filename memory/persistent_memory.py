import json
import os

MEMORY_FILE = "memory/runtime_memory.json"

def default_memory():

    return {
        "states": [],
        "transitions": []
    }

def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return default_memory()

    try:

        with open(MEMORY_FILE) as f:
            data = json.load(f)

        if not isinstance(data,dict):
            return default_memory()

        if "states" not in data:
            data["states"] = []

        if "transitions" not in data:
            data["transitions"] = []

        return data

    except:
        return default_memory()

def save_memory(memory):

    with open(MEMORY_FILE,"w") as f:
        json.dump(memory,f,indent=4)

def register_state(memory,state):

    if "states" not in memory:
        memory["states"] = []

    memory["states"].append(state)

    if len(memory["states"]) > 100:
        memory["states"] = memory["states"][-100:]

def register_transition(memory,old,new):

    if "transitions" not in memory:
        memory["transitions"] = []

    memory["transitions"].append({
        "from": old,
        "to": new
    })

    if len(memory["transitions"]) > 100:
        memory["transitions"] = (
            memory["transitions"][-100:]
        )
