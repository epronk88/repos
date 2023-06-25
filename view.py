#!/usr/bin/env python3

from flask import Flask, render_template
from test import parser
import os

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def home():
    parser()
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)