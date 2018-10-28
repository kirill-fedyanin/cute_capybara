# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

@app.route('/', methods=['GET'])
def hello_world():
    return 'Diana is cute developer ^_^'


def button():
    return {
        "text": "Mi-mi-mi",
        "url": "http://fedyanin.me/",
        "payload": {}
    }

class BabyStorage:
    def __init__(self):
        self.storage = [
            {
                'name': 'капибара',
                "image_id": "965417/d8a1988af5c2a38ba693",
                'level': 1
            },
            {
                'name': 'бобер',
                'image_id': '965417/e509419a31cfecf7ff5a',
                'level': 1
            }
        ]


class Master:
    def __init__(self):
        pass

    def reply(self, request_json, response):
        card = self._make_card("965417/d8a1988af5c2a38ba693")
        response['response']['text'] = 'You are cute!'
        response['response']['card'] = card


    def _make_card(self, image_id):
        return {
            "type": "BigImage",
            "image_id": image_id,
            "title": "Capybara",
            "description": "Can you find someone more cute?",
        }


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
        # handle_dialog(request.json, response)

        return json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )



def handle_dialog(req, res):
    print(req)
    card = {
        "type": "BigImage",
        "image_id": "965417/d8a1988af5c2a38ba693",
        "title": "Capybara",
        "description": "Can you find someone more cute?",
    }
    # if req['request']['original_utterance'].lower() in [
    #     'ладно',
    #     'куплю',
    #     'покупаю',
    #     'хорошо',
    # ]:


    res['response']['text'] = 'You are cute!'
    res['response']['card'] = card
    return

requester = Requester()

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])
def main():
# Функция получает тело запроса и возвращает ответ.
#     logging.info('Request: %r', request.json)
    response = requester.parse()
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')


#
# # Функция для непосредственной обработки диалога.
# def handle_dialog(req, res):
#     user_id = req['session']['user_id']
#
#     if req['session']['new']:
#         # Это новый пользователь.
#         # Инициализируем сессию и поприветствуем его.
#
#         sessionStorage[user_id] = {
#             'suggests': [
#                 "Не хочу.",
#                 "Не буду.",
#                 "Отстань!",
#             ]
#         }
#
#         res['response']['text'] = 'Привет! Купи слона!'
#         res['response']['buttons'] = get_suggests(user_id)
#         return
#
#     # Обрабатываем ответ пользователя.
#     if req['request']['original_utterance'].lower() in [
#         'ладно',
#         'куплю',
#         'покупаю',
#         'хорошо',
#     ]:
#         # Пользователь согласился, прощаемся.
#         res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!'
#         return
#
#     # Если нет, то убеждаем его купить слона!
#     res['response']['text'] = 'Все говорят "%s", а ты купи слона!' % (
#         req['request']['original_utterance']
#     )
#     res['response']['buttons'] = get_suggests(user_id)
#
# # Функция возвращает две подсказки для ответа.
# def get_suggests(user_id):
#     session = sessionStorage[user_id]
#
#     # Выбираем две первые подсказки из массива.
#     suggests = [
#         {'title': suggest, 'hide': True}
#         for suggest in session['suggests'][:2]
#     ]
#
#     # Убираем первую подсказку, чтобы подсказки менялись каждый раз.
#     session['suggests'] = session['suggests'][1:]
#     sessionStorage[user_id] = session
#
#     # Если осталась только одна подсказка, предлагаем подсказку
#     # со ссылкой на Яндекс.Маркет.
#     if len(suggests) < 2:
#         suggests.append({
#             "title": "Ладно",
#             "url": "https://market.yandex.ru/search?text=слон",
#             "hide": True
#         })
#
#     return suggests
