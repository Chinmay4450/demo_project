from flask import Flask
from . import lineage
def create_app():
    app = Flask(__name__) 
    app.register_blueprint(lineage.lineage)
    return app



