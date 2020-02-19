from flask import Flask, render_template
import random
import os

app = Flask(__name__)

@app.route('/')
def index():

    namer_text = os.popen('python3 /usr/src/app/namer.py').read()
    return(render_template('index.html', namer_text=namer_text))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
