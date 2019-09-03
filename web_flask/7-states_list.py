#!/usr/bin/python3
"""starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def index():
    my_dict = storage.all('State')
    return render_template('7-states_list.html', mydict=my_dict)


@app.teardown_appcontext
def teardown():
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
