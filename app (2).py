import numpy as np
import pickle
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
model = pickle.load(open(r"C:\Users\yuvar\OneDrive\Desktop\Asteroid classification\Asteroid_classification.pkl",'rb'))
column=pickle.load(open(r"C:\Users\yuvar\OneDrive\Desktop\Asteroid classification\asteroid.pkl",'rb'))

@app.route('/')# route to display the home page
def home():
    return render_template('index.html') #rendering the home page
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/predict',methods=["POST","GET"])# route to showinput_feature=[float(x) for x in request.form.values() ] the predictions in a web UI
def predict():
    x = [int(x) for x in request.form.values()]
    x=np.array(x)
    predict=model.predict([x])
    if (predict==0):
        return render_template("predict.html",predict="Its Harmfull to our Earth]")
    else:
        return render_template("predict.html",predict="Its Not Harmfull to Earth")
if __name__=="__main__":
   app.run(debug = True,port = 1212)
