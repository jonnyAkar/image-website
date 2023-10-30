from flask_cors import CORS
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():

    return render_template('index.html')


app.run(debug=True)