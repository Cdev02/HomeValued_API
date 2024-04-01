from flask import Flask
from config import config
from routes import property
from flask_cors import CORS
import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
path_root1 = Path(__file__).parents[0]
sys.path.append(str(path_root))
sys.path.append(str(path_root1))


app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost"}})


def page_not_found(error):
    return "<h1>Welcome to HomeValued Inc.</h1>", 404


if __name__ == "__main__":
    app.config.from_object(config["development"])

    # Blueprints
    app.register_blueprint(property.main, url_prefix="/api/properties")

    app.register_error_handler(404, page_not_found)

    app.run(host="0.0.0.0", port=int("5002"))
