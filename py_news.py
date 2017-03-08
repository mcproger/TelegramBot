import vk
import json
import time
import getpass

id_app = getpass.getpass('Enter App id: ')
login = getpass.getpass('Enter login: ')
password = getpass.getpass('Enter password: ')

def vkAutorization():
    session = vk.AuthSession(id_app, login, password,  scope='wall, messages, groups')
    vk_api = vk.API(session)
    return vk_api

def id_groups_load():
    filename = 'groups_id.json'
    with open(filename, mode='r', encoding='utf-8') as myfile:
        data = json.load(myfile)

        return data

def add_python_news():
    news = []
    post = {}
    python_news = []
    for id in id_groups_load():
            post = vkAutorization().wall.search(owner_id=-id['owner_id'], query='Python', extended='1', count='1')['wall'][1]
            news.append(post)
            post = {}
            for posts in news:
                if ((time.time() - posts['date']) <= 86400) and (posts['from_id'] == posts['to_id']) and (posts['post_type'] != 'copy'):
                    post = posts
                    python_news.append(post)
                    post = {}
                    del news[0]
    return python_news

if __name__ == "__main__":
    py_posts = add_python_news()
    filename = 'python_posts'
    with open(filename, mode='w', encoding='utf-8') as myfiles:
        json.dump(py_posts, myfiles)







