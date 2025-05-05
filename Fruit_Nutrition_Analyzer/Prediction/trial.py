import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image
fm=load_model("Z:\College Stuff\FlowTest\modelfinal.h5")
img = tf.keras.utils.load_img(r"Z:\Watermelon.jpg", grayscale=False, target_size=(224,224))
x= tf.keras.utils.img_to_array(img)
x= np.expand_dims(x, axis=0)
img_preprocessed = preprocess_input(x)
pred=fm.predict(img_preprocessed)
result=pred[0]
if result[0]==1.0:
    print("Apple")
elif result[1]==1.0:
    print("Lychee")
elif result[2]==1.0:
    print("Pear")
else:
    print("Watermelon")

