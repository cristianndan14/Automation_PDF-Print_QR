from flask import Flask
from flask_mysqldb import MySQL

from .routes.index import init_index
from .routes.output import init_output


app = Flask(__name__)

db = MySQL(app)

init_index(app, db)
init_output(app, db)

def run_app(config):
    app.config.from_object(config)
    return app
