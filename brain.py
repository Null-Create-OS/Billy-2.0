import os
import time

os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

from sentence_transformers import SentenceTransformer
import numpy as np


def loading_screen():

    print("""
╔══════════════════════════════╗
║                              ║
║        BILLY 2.0             ║
║        AI CORE BOOT          ║
║                              ║
╚══════════════════════════════╝
""")

    steps = [
        "Initializing memory",
        "Loading language model",
        "Connecting neural pathways",
        "Preparing understanding system",
        "Starting personality module"
    ]

    for step in steps:

        print(step)

        for i in range(20):
            print("#", end="", flush=True)
            time.sleep(0.03)

        print(" ✓")


loading_screen()


print("\n🧠 Loading Billy's brain...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("✅ Billy's brain loaded!\n")


def understand(text):

    return model.encode(text)


def similarity(a,b):

    return np.dot(a,b) / (
        np.linalg.norm(a)
        *
        np.linalg.norm(b)
    )