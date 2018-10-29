# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

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
            'Ну что, попробуем? Как называет вот этот зверь?'
        )

    def get_right(self):
        return(
            'Отлично!\n\nА теперь попробуй отгадать этого'
        )

    def get_wrong(self):
        return(
            'Хм, неверно, попробуй ещё'
        )

    def win(self):
        return(
            'Ты отгадал всех-превсех. Держи медаль'
        )


class Master:
    def __init__(self):
        self.texts = TextBook()

    def reply(self, req):
        img_id = "965417/d8a1988af5c2a38ba693"
        if req['session']['new']:
            text = self.texts.get_start()
        else:
            text = self.texts.get_right()

        res = {
            "version": req['version'],
            "session": req['session'],
            "response": {
                "text": text,
                "card": self._make_card(img_id, text),
                "end_session": False,
            }
        }

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



