import tensorflow as tf
import keras
from keras.models import load_model

import numpy as np
import NetworkDataUtils as NWD

def trainNetwork(dataPrefix):
    #Load Network Data
    train_data, train_labels, inputRange = NWD.getNetworkData("Data/FaceEvaluations/" + dataPrefix + ".txt", " ");
    train_data = np.array(train_data)
    train_labels = np.array(train_labels)

    #Setup Neural Network Structure (Model)
    model = keras.Sequential()
    model.add(keras.layers.Dense(123, input_shape=(123,), activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(123, activation=tf.nn.sigmoid))
    model.add(keras.layers.Dense(5, activation=tf.nn.sigmoid))

    #Compile The Network using an Adam Optimizer with a small learning rate (Standard: lr=0.01)
    model.compile(optimizer=keras.optimizers.Adam(lr=0.05, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.001, amsgrad=False),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    #Train the model on the data with a large epochs and no validation split.
    history = model.fit(train_data,
                        train_labels,
                        epochs=50000,
                        batch_size=550,
                        #validation_split=0.00,
                        verbose=0)
    #model.summary()
    #Save the model to a file
    model.save("Data/Models/" + dataPrefix + '.h5')

def evaluate(dataPrefix):
    #get network data for evaluating
    train_data, train_labels, inputRange = NWD.getNetworkData("Data/FaceEvaluations/" + dataPrefix + ".txt", " ");
    train_data = np.array(train_data)
    train_labels = np.array(train_labels)

    #Load Model
    model = load_model("Data/Models/" + dataPrefix + ".h5")

    results = model.evaluate(x=train_data, y=train_labels, batch_size=550, verbose=0)
    print("Evaluation: \n" + str(results))
    results = model.predict(train_data, batch_size=512, verbose=0, steps=None)

    print("Accuracy: \n" + str(NWD.getNetworkAccuracy(results, train_labels)))

    print("Guess Count: \n" + str(NWD.getResultCount(results)))