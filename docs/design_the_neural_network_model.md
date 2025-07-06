### **Building the Neural Network Model**

```python
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(trainX[0]),), activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(trainY[0]), activation='softmax'))
```
- **Model Architecture**:
    - **Input Layer**: Dense layer with 128 neurons and input equal to the size of the vocabulary (`len(trainX[0])`), using ReLU activation. 
    - **Dropout Layers**: Dropout with a rate of 50% to reduce overfitting during training.
    - **Hidden Layer**: Dense layer with 64 neurons and ReLU activation.
    - **Output Layer**: Dense layer with the number of outputs equal to the number of intent categories (`len(trainY[0])`), using softmax activation for multiclass classification.

### **Compiling the Model**
```python
sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
```
- **Optimizer**: SGD (Stochastic Gradient Descent) with a learning rate of 0.01, momentum of 0.9, and Nesterov acceleration.
- **Loss Function**: Categorical crossentropy is used for multiclass classification.
- **Metric**: Accuracy is used to measure model performance during training.

### **Training the Model**

```python
hist = model.fit(np.array(trainX), np.array(trainY), epochs=200, batch_size=5, verbose=1)
```

- **`fit()`**: Trains the model.
    - **Inputs**: `trainX` (word vectors) and `trainY` (intent one-hot vectors).
    - **`epochs=200`**: Number of full passes through the dataset.
    - **`batch_size=5`**: Number of training examples used in each training step.
    - **`verbose=1`**: Displays training progress.

### **Saving the Trained Model**

```python
model.save('chatbot_model.h5', hist)
print('Done')
```

- Saves the trained model as an HDF5 file (`chatbot_model.h5`) for later predictions.
- Prints "Done" after successfully completing the process.
