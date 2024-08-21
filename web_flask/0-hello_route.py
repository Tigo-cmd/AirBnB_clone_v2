#!/usr/bin/python3
"""A script that starts flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
