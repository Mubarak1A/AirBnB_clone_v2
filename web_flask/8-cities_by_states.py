#!/usr/bin/python3
"""starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def index():
    my_dict = storage.all()
    return render_template('8-cities_by_states.html', mydict=my_dict)


@app.teardown_appcontext
def teardown(tmp):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
