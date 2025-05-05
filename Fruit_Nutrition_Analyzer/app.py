from flask import Flask, render_template, url_for, request
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image
UPLOAD_FOLDER = 'Z:\College Stuff\Sample'
app=Flask(__name__)
fm=load_model("Z:\College Stuff\Sample\Prediction\modelfinal.h5")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods=["POST","GET"])
def index():
    if request.method=="POST":
        pred_input=request.files["pred_img"]
        pred_input.filename = "pred.jpg"
        path = os.path.join(app.config['UPLOAD_FOLDER'], pred_input.filename)   
        pred_input.save(path)
        img = tf.keras.utils.load_img(r"Z:\College Stuff\Sample\pred.jpg", grayscale=False, target_size=(224,224))
        x= tf.keras.utils.img_to_array(img)
        x= np.expand_dims(x, axis=0)
        img_preprocessed = preprocess_input(x)
        pred=fm.predict(img_preprocessed)
        result=pred[0]
        if result[0]==1.0:
            return render_template("applepage.html")
        elif result[1]==1.0:
            return render_template("lycheepage.html")
        elif result[2]==1.0:
            return render_template("pearpage.html")
        else:
            return render_template("watermelonpage.html")
        
    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)