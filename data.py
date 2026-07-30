import numpy as np

vocab = {}

def add_to_vocab(word):
    if word not in vocab:
        vocab[word] = len(vocab)

def build_vocab(sentences):
    for sentence in sentences:
        for word in sentence.lower().split():
            add_to_vocab(word)

def text_to_vector(text):
    vec = np.zeros(len(vocab))
    for word in text.lower().split():
        if word in vocab:
            vec[vocab[word]] += 1
    return vec

def get_training_data():
    inputs = [
        "hello",
        "hi",
        "how are you",
        "bye"
    ]

    outputs = [
        [1],
        [1],
        [2],
        [0]
    ]

    # 🔥 FIX: build vocab FIRST
    build_vocab(inputs)

    # THEN vectorize
    X = np.array([text_to_vector(t) for t in inputs])
    y = np.array(outputs)

    return X, y