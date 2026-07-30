from brain import understand, similarity
from knowledge import load_knowledge


def respond(text):

    knowledge = load_knowledge()

    facts = knowledge["facts"]

    if not facts:
        return "I'm not sure yet. Can you teach me?"


    user_vector = understand(text)

    best_match = None
    best_score = 0


    for subject, information in facts.items():

        fact_text = f"{subject} is {information}"

        fact_vector = understand(fact_text)

        score = similarity(
            user_vector,
            fact_vector
        )

        if score > best_score:
            best_score = score
            best_match = (
                subject,
                information
            )


    if best_match and best_score > 0.45:

        subject, information = best_match

        return f"{subject.title()} is {information}."


    return "I'm not sure yet. Can you teach me?"