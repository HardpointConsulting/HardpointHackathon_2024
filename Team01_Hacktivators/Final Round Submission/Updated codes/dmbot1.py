import time
from instagrapi import Client
from dm_reply_check1 import dm_reply

user = input('Enter your username:')
passwd = input('Enter your Password:')
cl = Client()
cl.login(user, passwd)
while True:
    inbox = cl.direct_pending_inbox()
    inbox1 = cl.direct_threads(selected_filter="unread")
    print(inbox1)
    for msg in inbox:
        print(msg)
        print(msg.id)
        id = msg.id
        m = cl.direct_messages(msg.id, 20)
        print(m)
        print(m[0].text)
        rep = dm_reply(m[0].text)
        print(rep)
        cl.direct_answer(id, rep)
        time.sleep(10)
    for msg in inbox1:
        print(msg)
        print(msg.id)
        id = msg.id
        m = cl.direct_messages(msg.id, 20)
        print(m)
        print(m[0].text)
        rep = dm_reply(m[0].text)
        print(rep)
        cl.direct_answer(id, rep)
        time.sleep(10)