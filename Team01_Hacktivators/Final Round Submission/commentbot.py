import time
from instagrapi import Client
from check_comment import reply_comment


user = input('Enter your username:')
passwd = input('Enter your Password:')
url = input('Enter the post url:')
cl = Client()
cl.login(user, passwd)
media_id = cl.media_id(cl.media_pk_from_url(url))
# comment = cl.media_comment(media_id, "Test comment")
a = cl.media_comments(media_id)

for comment in a:
    print(comment.dict)
    # if 'Hello' in comment.text:
    #     cl.media_comment(media_id=media_id, text='Hi', replied_to_comment_id=comment.pk)
    #     print("commented")
    c = reply_comment(comment.text)
    cl.media_comment(media_id=media_id, text=c, replied_to_comment_id=comment.pk)
    print('commented')
    time.sleep(10)

# print(a)
# print(a['pk'])
# print(comment.dict)