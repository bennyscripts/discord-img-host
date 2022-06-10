# Made by @bentettmar

import flask

from utils import images

blueprint = flask.Blueprint("index", __name__, url_prefix="/")
db = images.Images()

@blueprint.route("/")
def index():
    return flask.render_template("index.html")

@blueprint.get("/<shorturl>")
def get(shorturl):
    img = db.get_img(shorturl)

    if img:
        return flask.render_template(
            "viewer.html", 
            image_filename=img["filename"],
            embed_title=img["embed"]["title"],
            embed_author=img["embed"]["author"],
            embed_description=img["embed"]["description"],
            embed_colour=img["embed"]["colour"],
            embed_image=img["url"]
        )

    return flask.jsonify({
        "error": "Image not found"
    })

@blueprint.get("/register")
def register():
    return flask.redirect("https://benny.fun/")