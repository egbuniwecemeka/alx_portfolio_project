#!/usr/bin/pythpn3
"""Entry point for EJ Farms"""

from api import create_app
from os import getenv

app = create_app()


if __name__ == "__main__":
    app.run(host=getenv('FLASK_HOST'), port=getenv('FLASK_PORT'), debug=True)
