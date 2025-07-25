from flask import Flask
import os

from QR import Texts

app = Flask(__name__)

@app.route('/')
def home():
    return Texts.render()

if __name__ == '__main__':
    app.run(debug=True)