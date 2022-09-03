# Made by @bentettmar

import os
import json
import flask

from utils import images
from utils import discord

blueprint = flask.Blueprint("api", __name__, url_prefix="/api")
db = images.Images()
config = json.load(open("data/config.json"))

@blueprint.post("/upload")
def upload():
    upload_key = config["auth"]["uploadKey"]
    
    if not upload_key: return flask.jsonify({"error": "Upload key not set"})
    if flask.request.headers.get("upload-key") != upload_key or not flask.request.headers.get("upload-key"): return flask.jsonify({"error": "Invalid upload key"})
    if not flask.request.files: return flask.jsonify({"error": "No file provided"})

    file = flask.request.files["file"]

    if file:
        filename = file.filename
        args = flask.request.form.to_dict()
        embed = {
            "title": args.get("embed-title", f"filename"),
            "author": args.get("embed-author", ""),
            "description": args.get("embed-description", ""),
            "colour": args.get("embed-colour", "000000")
        }

        file.save("data/cache/{}".format(filename))
        url = discord.upload_file("data/cache/{}".format(filename))
        os.remove("data/cache/{}".format(filename))
        
        short_url = db.add_img(url, embed)

        # get flask request domain
        domain = flask.request.headers.get("Host")
        protocol = "https" if flask.request.headers.get("X-Forwarded-Proto") == "https" else "http"
        short_url = f"{protocol}://{domain}/{short_url}"

        return short_url
