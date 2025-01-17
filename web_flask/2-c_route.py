#!/usr/bin/python3
"""starts a Flask web application """


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def index2():
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def index3(text):
        return "C {}".format(text).replace("_", " ")
    app.run(host='0.0.0.0')
