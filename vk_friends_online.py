import vk
import getpass
import settings

def get_user_login():
    return input('Your VK login: ')

def get_user_password():
    return getpass.getpass('\nYour VK password: ')

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=settings.APP_ID,
        user_login=login,
        user_password=password,
        scope = 2)

    api = vk.API(session)
    online_friends_ids = api.friends.getOnline()
    online_friends_info = api.users.get(user_ids = online_friends_ids, lang = 3)
    return [(friend['first_name'], friend['last_name']) for friend in online_friends_info]

def output_friends_to_console(friends_online):
    print('\nNow online:')
    for friend in friends_online:
        print('{} {}'.format(friend[0], friend[1]))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    online_friends_name_lastname = get_online_friends(login, password)
    output_friends_to_console(online_friends_name_lastname)