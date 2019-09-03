#!/usr/bin/python3
"""starts a Flask web application """


if __name__ == "__main__":
    from flask import Flask
    from flask import render_template
    from models import storage

    app = Flask(__name__)
    my_dict = storage.all('State')

    @app.route('/states_list', strict_slashes=False)
    def index():
        return render_template('7-states_list.html', mydict=my_dict)

    app.run(host='0.0.0.0')

    @app.teardown_appcontext
    def teardown():
        storage.close()
