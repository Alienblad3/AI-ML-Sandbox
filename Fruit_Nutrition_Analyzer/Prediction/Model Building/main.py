import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gpu_dev=tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpu_dev[0],True)
train_path= "Z:\College Stuff\Fruits\Trial\Trial Train"
test_path="Z:\College Stuff\Fruits\Trial\Trial Test"
train_batches=ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
    .flow_from_directory(directory=train_path,target_size=(224,224), classes=["Apple","Lychee","Pear","Watermelon"], batch_size=10)
valid_batches=ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
    .flow_from_directory(directory=test_path,target_size=(224,224), classes=["Apple","Lychee","Pear","Watermelon"], batch_size=10)
test_batches=ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
    .flow_from_directory(directory=test_path,target_size=(224,224), classes=["Apple","Lychee","Pear","Watermelon"], batch_size=10, shuffle=False)

model=Sequential([
    Conv2D(filters=32, kernel_size=(3,3), input_shape=(224,224,3), activation="relu", padding="same"),
    MaxPool2D(pool_size=(2,2), strides=2),
    Conv2D(filters=64, kernel_size=(3,3),activation="relu", padding="same"),
    MaxPool2D(pool_size=(2,2), strides=2),
    Flatten(),
    Dense(units=4, activation="softmax")
])
print(model.summary())
model.compile(optimizer=Adam(learning_rate=0.0001),loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(x=train_batches, validation_data= valid_batches, epochs=10, verbose=2)
model.save("modelfinal.h5")





