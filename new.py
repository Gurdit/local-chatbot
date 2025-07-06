import random #Used for shuffling data.
import json # Loads JSON files, typically to read intent data.
import pickle # Serializes and saves data structures for later use
import numpy as np # Numerical operations and array manipulations.
import tensorflow as tf # Builds and trains the machine learning model.

import nltk # Provides natural language processing functionalities.
from nltk.stem import WordNetLemmatizer # Reduces words to their base or root form (lemmatization).

# Load Data and Initialize Variables.
lemmatizer = WordNetLemmatizer() # An instance of the for processing words. `WordNetLemmatizer`

'''
Loads the intent structure from a JSON file (),
which contains predefined intents,
patterns, and responses. `intents.json`
'''
intents = json.loads(open('intents.json').read())

words =[] # Stores all words found in the dataset (processed later).
classes =[] # Holds all unique intent tags (categories).
documents = [] # A list storing tuples of patterns (tokenized input sentences) and their corresponding intent tags.
ignoreLetters = ['?', '!', '.', ','] # Characters to ignore during preprocessing.

# Tokenization and Lemmatization.
for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        documents.append((words, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignoreLetters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
outputEmpty = [0] * len(classes)

for document in documents:
    bag = []
    wordPatterns = document[0]
    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]
    for word in wordPatterns:
        bag.append(1) if word in wordPatterns else bag.append(0)

    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    training.append(bag + outputRow)

random.shuffle(training)
training = np.array(training)

trainX = training[:, :len(words)]
trainY = training[:, len(words):]

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(trainX[0]),), activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(trainY[0]), activation='softmax'))

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(trainX), np.array(trainY), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)
print('Done')