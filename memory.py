import json
import os
import re


MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "facts": {},
            "conversations": []
        }

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def remember(key, value):

    memory = load_memory()

    if key not in memory["facts"]:
        memory["facts"][key] = []


    if value not in memory["facts"][key]:
        memory["facts"][key].append(value)


    save_memory(memory)


def recall(key):
    memory = load_memory()

    return memory["facts"].get(key)


def add_conversation(user, billy):
    memory = load_memory()

    memory["conversations"].append({
        "user": user,
        "billy": billy
    })

    save_memory(memory)


# 🧠 Billy learns facts from normal sentences
def learn_from_sentence(sentence):

    sentence = sentence.lower()


    patterns = [
        r"my name is (.+)",
        r"i am called (.+)",
        r"you can call me (.+)",
        r"remember that my name is (.+)"
    ]


    for pattern in patterns:

        match = re.search(pattern, sentence)

        if match:
            name = match.group(1)

            remember(
                "name",
                name.title()
            )

            return f"Got it! I'll remember your name is {name.title()}."


    return None