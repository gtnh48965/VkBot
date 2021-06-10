import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='561bd020a5ac6f338b28a7f0b8e6b5551feedab442b1d1c6b791416b741ef7bc1d589933ae80ef06b4d66')
# тут токен группы
vk = vk_session.get_api()
longpol = VkLongPoll(vk_session)


def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but('Привет', 'positive'), get_but('Пока', 'positive')],
        [get_but('привет', 'positive'), get_but('пока', 'positive')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard})


def main():
    for event in longpol.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                id = event.user_id
                msg = event.text.lower()

                sender(id, msg.upper())


while True:
    main()