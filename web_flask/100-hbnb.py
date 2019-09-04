#!/usr/bin/python3
"""starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def index():
    state_dict = storage.all('State')
    amenity_dict = storage.all('Amenity')
    place_dict = storage.all('Place')
    user_dict = storage.all('User')
    return render_template('100-hbnb.html', state_dict=state_dict,
                           amenity_dict=amenity_dict, place_dict=place_dict,
                           user_dict= user_dict)


@app.teardown_appcontext
def teardown(tmp):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
