# Made by @bentettmar

import json
import random
import string

class Images:
    def __init__(self):
        self.json = json.load(open("data/images.json"))

    def add_img(self, url: str, embed: dict):
        short_url = self.generate_short_url()
        filename = url.split("/")[-1]

        self.json[short_url] = {
            "url": url,
            "filename": filename,
            "embed": embed
        }
        self.save()

        return short_url

    def get_img(self, short_url: str):
        return self.json.get(short_url)

    def generate_short_url(self):
        short_url = "".join(random.choice(string.ascii_lowercase) for i in range(8))
        
        while short_url in self.json:
            short_url = "".join(random.choice(string.ascii_lowercase) for i in range(8))
        
        return short_url

    def save(self):
        with open("data/images.json", "w") as f:
            json.dump(self.json, f, indent=4)