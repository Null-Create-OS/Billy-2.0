from response import respond
from memory import (
    add_conversation,
    recall,
    learn_from_sentence
)
from learning import learn_from_text


print("Billy 2.0 online 🧠")


def handle_memory(user):

    text = user.lower()


    # User identity questions
    if (
        "my name" in text
        or "who am i" in text
        or "do you remember me" in text
    ):

        name = recall("name")

        if name:
            return f"Your name is {name}."

        return "I don't know your name yet."


    # Billy identity questions
    if (
        "your name" in text
        or "who are you" in text
    ):

        return "My name is Billy 2.0!"


    # User teaching Billy their name
    learned_memory = learn_from_sentence(user)

    if learned_memory:
        return learned_memory


    return None



while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    # Learn first
    learned = learn_from_sentence(user)

    if learned:
        print("Billy: I'll remember that! 🧠")
        add_conversation("User", user)
        continue

    # Check memory
    from memory import load_memory
    memory = load_memory()

    # Generate response
    reply = respond(user, memory)


    print("Billy:", reply)

    # Save conversation
    add_conversation("User", user)
    add_conversation("Billy", reply)