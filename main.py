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
        print("Billy: Goodbye! 👋")
        break



    # 1. Check memory first
    memory_reply = handle_memory(user)

    if memory_reply:

        print("Billy:", memory_reply)

        add_conversation(
            user,
            memory_reply
        )

        continue



    # 2. Check Billy's learned knowledge
    reply = respond(user)


    if reply != "I'm not sure yet. Can you teach me?":

        print("Billy:", reply)

        add_conversation(
            user,
            reply
        )

        continue



    # 3. Unknown information → try learning

    learned = learn_from_text(user)


    if learned:

        print("Billy:", learned)

        add_conversation(
            user,
            learned
        )

        continue



    # 4. Nothing worked

    print(
        "Billy:",
        "I'm not sure yet. Can you teach me?"
    )

    add_conversation(
        user,
        "I'm not sure yet. Can you teach me?"
    )