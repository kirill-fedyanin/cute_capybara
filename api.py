# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals
from random import choice

import json
from flask import Flask, request

from lib import BabyStorage

app = Flask(__name__)


# Хранилище данных о сессиях.
sessionStorage = {}


class TextBook:
    def get_start(self):
        return(
            'Привет. Правила простые - я буду показывать тебе картинки, а ты должен угадать имя животного на них.'
            'Ну что, попробуем?'
        )

    def get_right(self):
        return 'Отлично! Как называется зверь на этой фотографии?'

    def get_wrong(self):
        return 'Хм, неверно, попробуй ещё'

    def win(self):
        return 'Ты отгадал всех-превсех. Держи медаль'


class User:
    def __init__(self, id, new=False):
        self.id = id
        if new:
            self._user = {}
        else:
            self._user = sessionStorage[id]

    def dump(self):
        sessionStorage[id] = self._user


class CutieProvider:
    def __init__(self):
        self.cuties = self._cuties_list()

    def get_cutie(self):
        cutie = choice(self.cuties)
        return cutie

    @staticmethod
    def _cuties_list():
        return [
            {
                'id': 1,
                'image_id': "965417/d8a1988af5c2a38ba693",
                'names': ['Капибара']
            },
            {
                'id': 2,
                'image_id': "965417/e509419a31cfecf7ff5a",
                'names': ['Бобёр', 'Бобр', 'Бобер']
            },
        ]


class Master:
    def __init__(self):
        self.texts = TextBook()
        self.zoo = CutieProvider()

    def _start_message(self):
        text = self.texts.get_start()
        suggests_ = [{"title": "Начнём", "hide": True}]
        return text, suggests_

    def reply(self, req):
        cutie = self.zoo.get_cutie()
        suggests = []
        card = None

        if req['session']['new']:
            text, suggests = self._start_message()
        else:
            text = self.texts.get_right()
            card = self._make_card(cutie['image_id'], text)

        res = {
            "version": req['version'],
            "session": req['session'],
            "response": {
                "text": text,
                "end_session": False,
            }
        }

        if suggests:
            res['response']['buttons'] = suggests

        if card:
            res['response']['card'] = card


        return json.dumps(
            res,
            ensure_ascii=False,
            indent=2
        )

    def _make_items(self, image_id, text):
        return {
            "type": "ItemsList",
            "items": [
                {'image_id': image_id}
            ],
            "description": text,
            "footer": {
                "text": text
            }
        }

    @staticmethod
    def _make_card(image_id, text):
        return {
            "type": "BigImage",
            "image_id": image_id,
            "description": text
        }


master = Master()


@app.route('/', methods=['GET'])
def hello_world():
    return 'Diana is cute developer =^_^='


@app.route("/", methods=['POST'])
def main():
    return master.reply(request.json)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
