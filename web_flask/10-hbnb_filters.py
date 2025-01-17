#!/usr/bin/python3
"""starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def index():
    state_dict = storage.all('State')
    amenity_dict = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', state_dict=state_dict,
                           amenity_dict=amenity_dict)


@app.teardown_appcontext
def teardown(tmp):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
