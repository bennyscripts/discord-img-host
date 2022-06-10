# Made by @bentettmar

import flask
import os
import importlib

app = flask.Flask(__name__, template_folder='templates')
extra_files = ["data/images.json"]

for route_file in os.listdir("routes"):
    if route_file.endswith(".py"):
        lib = importlib.import_module("routes.{}".format(route_file[:-3]))
        app.register_blueprint(lib.blueprint)

if __name__ == "__main__":
    for _ in range(10):
        print("Made by @bentettmar")
    app.run(debug=True, extra_files=extra_files, host="0.0.0.0")