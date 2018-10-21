import requests

img_name = 'https://i.ytimg.com/vi/m9UE83BCROM/maxresdefault.jpg'
o_auth = 'AQAAAAABHv2XAAT7o2e3Q1LJnUWhuZG1vJrwlyw'
skill_id = '32dda7b4-b4f9-4517-8aa2-fd2853ea4385'
# base_url = 'https://dialogs.yandex.ru/developer/skills/'
base_url = 'https://dialogs.yandex.net/api/v1/'

headers = {
    'Authorization': f'OAuth {o_auth}'
}


def get_status():
    path = 'status'
    r = requests.get(base_url + path, headers=headers)
    print(r)
    print(r.text)


get_status()

# for line in lines:
#     word = line.split()[0]
#     words.append(word)
