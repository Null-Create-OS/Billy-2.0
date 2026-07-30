# 🧠 Billy 2.0

> A personal learning AI assistant built from scratch with memory, knowledge storage, language understanding, and adaptive learning.

Billy 2.0 is an experimental AI companion designed to learn from conversations, remember important information, and gradually become more personalized over time.

---

# ✨ Features

## 🗣️ Natural Conversation

Billy can understand text input and respond using semantic similarity rather than simple keyword matching.

Example:


You: Hello
Billy: Hey! Nice to see you.


Billy uses sentence embeddings to understand that similar phrases have similar meanings.

Example:


"Hello"
"Hey there"
"Hi"


are recognized as related ideas.

---

# 🧠 Memory System

Billy can remember information about the user.

Example:


You: My name is Yossel

Billy:
Got it! I'll remember your name is Yossel.


Later:


You: Who am I?

Billy:
Your name is Yossel.


Memory is stored permanently using JSON files.

---

# 📚 Knowledge Learning

Billy can learn facts from the user.

Example:


You:
The largest planet is Jupiter

Billy:
I learned that largest planet is Jupiter.


Later:


You:
What is the largest planet?

Billy:
Largest planet is Jupiter.


---

# 🧩 Architecture

Billy is separated into different modules:


Billy 2.0
│
├── main.py
│ └── Main conversation loop
│
├── brain.py
│ └── Language understanding
│
├── response.py
│ └── Generates responses
│
├── memory.py
│ └── Stores user information
│
├── learning.py
│ └── Detects and learns facts
│
├── knowledge.py
│ └── Stores learned information
│
├── data.py
│ └── Training data
│
└── *.json
└── Long-term storage


---

# 🧠 How Billy Thinks

Billy's processing pipeline:


User Input
|
v
Sentence Understanding
|
v
Memory Check
|
+------> Personal Memory
|
v
Knowledge Search
|
+------> Learned Facts
|
v
Response Generation
|
v
Billy Reply


---

# 💾 Memory Files

## memory.json

Stores personal information.

Example:

```json
{
    "facts": {
        "name": "Yossel"
    }
}
knowledge.json

Stores learned facts.

Example:

{
    "facts": {
        "largest planet": "Jupiter"
    }
}
⚙️ Installation
Requirements

Python 3.10+

Install dependencies:

pip install numpy
pip install requests
pip install sentence-transformers
▶️ Running Billy

Start Billy:

python main.py

Example:

Billy 2.0 online 🧠

You:
My name is Yossel

Billy:
Got it! I'll remember your name is Yossel.
🧪 Current Limitations

Billy is still an experimental AI system.

Currently:

Memory is rule-based
Learning uses simple pattern detection
Responses depend on stored knowledge
No true self-training neural model yet

Billy does not rewrite his own code or independently improve his intelligence.

🚀 Future Goals
🧠 Advanced Memory

Planned:

Memory importance ranking
Forgetting irrelevant information
Long-term personality development
Memory timestamps
Multiple users

Example:

{
 "fact": "User likes astronomy",
 "importance": 0.9,
 "source": "conversation"
}
🎤 Voice System

Future:

Wake word detection
Speech recognition
Text-to-speech
Natural voice personality

Example:

"Wake up, Billy."

Billy:
"I'm here!"
👁️ Vision System

Future:

Camera input
Object recognition
Scene understanding
Visual learning
🤖 Robot Integration

Possible future hardware:

Camera
Microphone
Speakers
Motors
Sensors

Billy could become a physical assistant.

🛠️ Development Philosophy

Billy is built around the idea:

An AI should not just answer questions. It should learn, remember, and grow with its user.

📜 Version History
Billy 2.0

Current version:

Added semantic language understanding
Added permanent memory
Added knowledge learning
Added modular architecture
Billy 1.0

Original version:

Neural network prototype
Basic training
Numeric prediction
👨‍💻 Creator

Created as a personal AI assistant experiment.

Project goal:

Build a curious, adaptive, and personalized AI companion.


Save this as:


README.md


in:


AGI/
│
├── README.md
├── main.py
├── brain.py
├── response.py
├── memory.py
├── learning.py
├── knowledge.py
└── data.py
