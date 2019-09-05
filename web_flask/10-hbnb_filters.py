#!/usr/bin/python3
"""Flask script"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False
st_id = None

@app.route('/hbnb_filters')
def index():
    """list of all State objects present in DBStorage sorted by name"""
    return render_template('10-hbnb_filters.py', s_l=storage.all("State"),a_l=storage.all("Amenities"))

@app.teardown_appcontext
def tear(self):
    """Close storage"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
