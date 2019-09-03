#!/usr/bin/python3
"""starts a Flask web application """


if __name__ == "__main__":
    from flask import Flask
    from flask import render_template

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

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def index6(n):
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def index7(n):
        return render_template('6-number_odd_or_even.html', n=n)
    app.run(host='0.0.0.0')
