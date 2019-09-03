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

    @app.route('/python/')
    @app.route('/python/<text>', strict_slashes=False)
    def index4(text="is cool"):
        return "Python {}".format(text).replace("_", " ")

    @app.route('/number/<int:n>', strict_slashes=False)
    def index5(n):
        return "{} is a number".format(n)
    app.run(host='0.0.0.0')
