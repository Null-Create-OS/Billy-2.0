import json
import os


FILE = "knowledge.json"


def load_knowledge():
    if not os.path.exists(FILE):
        return {"facts": {}}

    with open(FILE, "r") as f:
        return json.load(f)


def save_knowledge(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def learn_fact(subject, information):

    knowledge = load_knowledge()

    knowledge["facts"][subject.lower()] = information

    save_knowledge(knowledge)


def get_fact(subject):

    knowledge = load_knowledge()

    return knowledge["facts"].get(subject.lower())