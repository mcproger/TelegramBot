import vk
import json
import time
import getpass

filename = 'groups_id.json'
with open(filename, mode="w", encoding='utf-8') as myfile:

    id_app = getpass.getpass('Enter App id: ')
    login = getpass.getpass('Enter login: ')
    password = getpass.getpass('Enter password: ')
    def vkAutorization():
        session = vk.AuthSession(id_app, login, password,  scope='wall, messages, groups')
        vk_api = vk.API(session)
        return vk_api

    def group_request():
        search = ['Python']
        groups = vkAutorization().groups.search(q='Python', count='10', extended='1')
        del groups[0]
        return groups

    def python_groups_id():
        id_group = []
        owner_id = {}
        for group in group_request():
            if group['is_closed'] == 0:
                newses = vkAutorization().wall.search(owner_id=-group['gid'], query='Python', extended='1')['wall']
                time.sleep(1)
                del newses[0]
                for news in newses:
                    if ((time.time() - news['date']) <= 86400):
                            print(group['gid'], group['name'])
                            owner_id['owner_id'] = group['gid']
                            id_group.append(owner_id)
                            owner_id = {}
                            break
        return id_group

    if __name__ == "__main__":
        json.dump(python_groups_id(), myfile)

