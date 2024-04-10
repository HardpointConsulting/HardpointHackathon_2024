import time
from instagrapi import Client
from dm_reply_check import dm_reply

user = input('Enter your username:')
passwd = input('Enter your Password:')
cl = Client()
cl.login(user, passwd)
inbox = cl.direct_pending_inbox()
for msg in inbox:
    print(msg)
    print(msg.id)
    id = msg.id
    msg = cl.direct_messages(msg.id, 20)
    print(msg)
    print(msg.text[0])
    rep = dm_reply(msg.text[0])
    print(rep)
    cl.direct_answer(id, rep)
    time.sleep(30)