# coding: utf-8
# Python's version: 3.5
# Задача 1: Сравнение предложений

import re
import numpy as np
from scipy.spatial.distance import cosine


def prepare_text():
    with open("sentences.txt", "r") as file:
        text = {}
        sentence_count = 0
        for line in file:
            line = line.lower()
            line = re.split(r"[^a-z]*", line)
            while "" in line:
                ind = line.index("")
                line.remove(line[ind])
            text[sentence_count] = line
            sentence_count += 1
    return text


def tokenize_text(text):
    tokens = {}
    d = 0
    for key in text.keys():
        for word in text[key]:
            if word not in tokens:
                tokens[word] = d
                d += 1
    return tokens


def create_matrix(text, tokens):
    matrix = np.zeros((len(text), len(tokens)))
    for key in text.keys():
        sentence = text[key]
        for tok_word in tokens.keys():
            count = 0
            for word in sentence:
                if word == tok_word:
                    count += 1
            matrix[key, tokens[tok_word]] = count
    return matrix


def compute_distance(sentence, matrix):
    distances = {}
    for i in range(1, matrix.shape[0]):
        distances[i] = cosine(sentence, matrix[i])
    return distances



if __name__ == "__main__":
    text = prepare_text()
    tokens = tokenize_text(text)
    matrix = create_matrix(text, tokens)
    distances = compute_distance(matrix[0], matrix)
    distances = sorted(distances.items(), key=lambda item: item[1])
    print(distances[0], distances[1])


