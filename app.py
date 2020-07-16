from flask import Flask, render_template, request
import pickle

import warnings
warnings.filterwarnings("ignore")


classfier = pickle.load(open("sentiment_analysis","rb"))
cv = pickle.load(open("cv-transform.pkl","rb"))

app = Flask(__name__)

@app.route('/')


if __name__ == '__main__':
	app.run(debug=True)