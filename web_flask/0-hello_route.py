#!/usr/bin/python3
"""A script that starts flask web application
Configure the file web_flask/0-hello_route.py to serve its content 
from the route /airbnb-onepage/ on port 5000.
"""

from flask import Flask

#create a flask application
app = Flask(__name__)

#
@app.route('/airbnb-onepage/')
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
