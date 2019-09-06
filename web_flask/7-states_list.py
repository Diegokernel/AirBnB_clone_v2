#!/usr/bin/python3
"""Flask script"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """list of all State objects present in DBStorage sorted by name"""
    return render_template('7-states_list.html', slist=storage.all("State"))


@app.teardown_appcontext
def tear(self):
    """Close storage"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
