import requests
import json


# img_name = 'https://i.ytimg.com/vi/m9UE83BCROM/maxresdefault.jpg'
img_name = 'https://i.pinimg.com/236x/6e/bf/98/6ebf98d450b65f8e40d7702cdc0c4c68--skunks-rodents.jpg'
o_auth = 'AQAAAAABHv2XAAT7o2e3Q1LJnUWhuZG1vJrwlyw'
skill_id = '32dda7b4-b4f9-4517-8aa2-fd2853ea4385'
base_url = 'https://dialogs.yandex.net/api/v1/'


headers = {
    'Authorization': 'OAuth ' + o_auth
}


def launch():
    upload_by_link(img_name)


def upload_by_link(link):
    # path = 'skills/' + skill_id + '/images'
    # headers['Content-Type'] = 'application/json'
    # data = {'url': link}
    # print(data)
    # print(headers)
    # print(base_url + path)
    # r = requests.post(base_url + path, data=data, headers=headers)
    # print(r)
    # print(r.text)

    r = requests.post(
        'https://dialogs.yandex.net/api/v1/skills/32dda7b4-b4f9-4517-8aa2-fd2853ea4385/images',
        data=json.dumps({'url': img_name}),
        headers={
            'Authorization': 'OAuth AQAAAAABHv2XAAT7o2e3Q1LJnUWhuZG1vJrwlyw',
            'Content-Type': 'application/json'
        }
    )
    print(r)
    print(r.text)



def get_status():
    path = 'status'
    r = requests.get(base_url + path, headers=headers)
    print(r)
    print(r.text)


if __name__ == '__main__':
    launch()

# for line in lines:
#     word = line.split()[0]
#     words.append(word)
