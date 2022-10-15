from flask import Flask, jsonify, make_response, Response, render_template
from flask_restful import Api
from models.repository import RepositoryAnime
from utils import convert
import json

app = Flask(__name__, template_folder="templates")
api = Api(app)
# app.json_encoder = FlaskJSONEncoder


@app.errorhandler(404)
def not_found(error) -> Response:
    return make_response(
        jsonify({"Status": 404, "Message": "Resource not found."}), 404
    )


@app.route("/", methods=["GET"])
@app.route("/api/v1/resources/home", methods=["GET"])
def home() -> str:
    return render_template("index.html")


@app.route("/api/v1/resources/animes", methods=["GET"])
def lists():
    _data: list = convert(RepositoryAnime().read())
    return jsonify({"Status": 200, "data": _data})


if __name__ == "__main__":
    app.run(debug=True)
