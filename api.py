# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

import json
import logging
from flask import Flask, request

from lib import BabyStorage

app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}


def button():
    return {
        "text": "Mi-mi-mi",
        "url": "http://fedyanin.me/",
        "payload": {}
    }


class Master:
    def __init__(self):
        pass

    def reply(self, request_json, response):

        # response['response']['text'] = 'You are cute!'
        response['response']['card'] = self._make_card("965417/d8a1988af5c2a38ba693")

    def _make_card(self, image_id):
        return {
            "type": "BigImage",
            "image_id": image_id,
        }
        # "title": "Capybara",
        # "description": "Can you find someone more cute?",


class Requester:
    def __init__(self):
        self.master = Master()

    def make_request(self):
        pass

    def parse(self):
        response = {
            "version": request.json['version'],
            "session": request.json['session'],
            "response": {
                "end_session": False
            }
        }

        self.master.reply(request.json, response)

        return json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )


requester = Requester()


@app.route('/', methods=['GET'])
def hello_world():
    return 'Diana is cute developer =^_^='


@app.route("/", methods=['POST'])
def main():
    response = requester.parse()
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')



