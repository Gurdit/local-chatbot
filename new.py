import os
import json
import pickle
import random
import nltk
import numpy as np
import tensorflow as tf
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load intents.json
intents_path = os.path.join(base_dir, 'intents.json')
if not os.path.exists(intents_path):
    raise FileNotFoundError(f"File {intents_path} not found.")
intents = json.loads(open(intents_path).read())

words = []  # Vocabulary
classes = []  # Unique intent tags
documents = []  # Patterns and tags
ignoreLetters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = [w for w in nltk.word_tokenize(pattern) if w not in ignoreLetters]
        words.extend(wordList)
        documents.append((wordList, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Process vocabulary and tags
words = sorted(set(lemmatizer.lemmatize(word.lower()) for word in words))
classes = sorted(set(classes))

# Pickle the results
words_file = os.path.join(base_dir, 'words.pkl')
classes_file = os.path.join(base_dir, 'classes.pkl')
pickle.dump(words, open(words_file, 'wb'))
pickle.dump(classes, open(classes_file, 'wb'))

# Training data
training = []
outputEmpty = [0] * len(classes)

for document in documents:
    bag = [1 if word in document[0] else 0 for word in words]
    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    training.append(bag + outputRow)

random.shuffle(training)
training = np.array(training)
trainX = training[:, :len(words)]
trainY = training[:, len(words):]

# Build the model
model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(len(trainX[0]),)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(trainY[0]), activation='softmax'))

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(trainX, trainY, epochs=200, batch_size=5, verbose=1)

# Save the model
model.save(os.path.join(base_dir, 'chatbot_model.keras'))
print("Model training complete. Model and pickle files saved.")