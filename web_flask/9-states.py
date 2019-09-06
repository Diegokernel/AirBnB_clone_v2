#!/usr/bin/python3
"""Flask script"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False
st_id = None

@app.route('/states')
def states_list():
    """list of all State objects present in DBStorage sorted by name"""
    return render_template('9-states.html', slist=storage.all("State"), st_id=st_id)

@app.route('/states/<string:st_id>')
def states_id(st_id):
        """Flask template states"""
            return render_template('9-states.html', slist=storage.all("State"), s_id=s_id)

@app.teardown_appcontext
def tear(self):
    """Close storage"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
