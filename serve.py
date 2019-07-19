import sys, json
from datetime import datetime

import flask
from flask import request

app = flask.Flask(__name__)
port = int(sys.argv[1]) if len(sys.argv) == 2 else 80

@app.route('/')
def index():
  return flask.render_template("index.html")

@app.route('/resume')
def resume():
  return flask.render_template("index.html")

if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run(host='0.0.0.0', port=port, debug=(port != 80))
