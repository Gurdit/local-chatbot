### **Preparing Training Data**
```python
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
```
- **`training`**: List to store the training data.
- **One-Hot Encoding Words (`bag`)**:
    - The model uses a "bag of words" approach: a binary vector representation of whether a word exists in the training vocabulary.

- **One-Hot Encoding Classes (`outputRow`)**:
    - Creates an output vector for the current intent, where the index corresponding to the document's tag is 1 and all others are 0.

- Combines the word vector (`bag`) and the output vector (`outputRow`) for each document, forming a training instance.

### **Shuffling and Converting Data to Numpy Arrays**

```python
random.shuffle(training)
training = np.array(training)
trainX = training[:, :len(words)]
trainY = training[:, len(words):]
```
- 
- **Shuffling**: Randomizes the training data to avoid any order bias during training.
- **Splitting**:
    - `trainX`: Contains input data (the word vectors).
    - `trainY`: Contains output data (the intent/category vectors).
