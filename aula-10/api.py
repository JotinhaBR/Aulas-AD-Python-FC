from __future__ import print_function
import sys
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    print('Test diojwdpoajdw', file=sys.stdout)
    return 'Hello, World!'