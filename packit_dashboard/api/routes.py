from flask import Blueprint, jsonify, request
from packit_dashboard.utils import return_json
from packit_dashboard.config import API_URL

api = Blueprint("api", __name__)

# The react frontend will request information here instead of fetching directly
# from the main API.
# This is because it will be easier to implement caching API requests here.
# (Flask-Caching etc)


@api.route("/api/copr-builds/")
def copr_builds():
    page = request.args.get("page")
    per_page = request.args.get("per_page")
    url = f"{API_URL}/copr-builds?page={page}&per_page={per_page}"
    return jsonify(return_json(url))


@api.route("/api/testing-farm/")
def testing_farm():
    page = request.args.get("page")
    per_page = request.args.get("per_page")
    url = f"{API_URL}/testing-farm/results?page={page}&per_page={per_page}"
    return jsonify(return_json(url))
