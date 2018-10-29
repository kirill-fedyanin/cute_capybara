# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

import json
from flask import Flask, request

from lib import BabyStorage

app = Flask(__name__)


# Хранилище данных о сессиях.
sessionStorage = {}


class Master:
    def __init__(self):
        pass

    def reply(self, request_):
        img_id = "965417/d8a1988af5c2a38ba693"
        response = {
            "version": request_.json['version'],
            "session": request_.json['session'],
            "response": {
                "end_session": False,
                "card": self._make_card(img_id)
            }
        }

        return json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )

    @staticmethod
    def _make_card(image_id):
        return {
            "type": "BigImage",
            "image_id": image_id,
        }


master = Master()


@app.route('/', methods=['GET'])
def hello_world():
    return 'Diana is cute developer =^_^='


@app.route("/", methods=['POST'])
def main():
    return master.reply(request)


if __name__ == "__main__":
    app.run(host='0.0.0.0')



