import re
from knowledge import learn_fact


def learn_from_text(text):

    text_lower = text.lower().strip()

    # Ignore questions
    question_words = [
        "what",
        "who",
        "where",
        "when",
        "why",
        "how",
        "is"
    ]

    if text_lower.endswith("?") or text_lower.split()[0] in question_words:
        return None


    patterns = [
        r"the (.+?) is (.+)",
        r"(.+?) is (.+)"
    ]


    for pattern in patterns:

        match = re.search(
            pattern,
            text_lower
        )

        if match:

            subject = match.group(1).strip()
            information = match.group(2).strip()


            # Avoid nonsense memories
            if subject in question_words:
                return None


            learn_fact(
                subject,
                information
            )

            return f"I learned that {subject} is {information}."


    return None