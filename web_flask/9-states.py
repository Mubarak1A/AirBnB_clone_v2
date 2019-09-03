#!/usr/bin/python3
"""starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def index(id=None):
    my_dict = storage.all()
    return render_template('9-states.html', mydict=my_dict, id=id)


@app.teardown_appcontext
def teardown(tmp):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
