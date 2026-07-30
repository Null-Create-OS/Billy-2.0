# response.py

import random


def respond(user, memory=None):

    if memory is None:
        memory = {}

    text = user.lower().strip()


    # Name memory
    if (
        "who am i" in text
        or "what is my name" in text
        or "whats my name" in text
        or "what's my name" in text
    ):

        name = memory.get("name")

        if name:
            return f"Your name is {name} 🧠"

        return "I don't know your name yet."


    # Greetings
    if any(x in text for x in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello! 😊",
            "Hey! Good to see you!",
            "Hi! What are we learning today?"
        ])


    if "how are you" in text:
        return "I'm running great! My neural pathways are active 🧠"


    if "what are you" in text:
        return (
            "I'm Billy 2.0, a learning AI assistant. "
            "I can remember information and improve over time."
        )


    return (
        "That's interesting! I'm still learning. "
        "Can you teach me more? 🧠"
    )