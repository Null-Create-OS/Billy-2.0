# memory.py

import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)


def recall(key):
    memory = load_memory()
    return memory.get(key)


def add_conversation(role, message):
    memory = load_memory()

    if "conversation" not in memory:
        memory["conversation"] = []

    memory["conversation"].append({
        "role": role,
        "message": message
    })

    save_memory(memory)


def learn_from_sentence(sentence):

    text = sentence.lower()

    if "my name is" in text:

        name = (
            sentence.lower()
            .replace("my name is", "")
            .strip()
            .title()
        )

        remember("name", name)

        return True

    return False