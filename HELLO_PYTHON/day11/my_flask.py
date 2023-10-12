from flask import Flask, request
from flask.templating import render_template
from astropy.io.misc.yaml import name
import pymysql
app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello JongChan!'

if __name__ == '__main__':
    app.run(debug=True)