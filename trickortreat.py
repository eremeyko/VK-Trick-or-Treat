from requests import post
from os import system
from time import sleep


def getFriends(access_token):

    friendsList = post('https://api.vk.com/method/apps.getLeaderboard', data={
        'api_id': 7968630,
        'method': 'apps.getLeaderboard',
        'format': 'json',
        'v': 5.131,
        'access_token': access_token,
        'type': 'score',
        'global': 0,
        'request_id': 'friends_result'
    }).json()

    if friendsList.get('response'):
        friendsList = friendsList['response']['items']
        usersIds = []

        for friend in friendsList:
            usersIds.append(friend['user_id'])

        return usersIds

    else:
        print('[!]Токен невалид')
        system('exit')


def sendTreat(users, access_token, treat=0, treatSended=0, flood=0,):

    for user in users:
        system('cls')
        print(f"""[•] Пользователей: {len(users)}
[>] Отправлено сладостей скриптом: {treat}
[+] Отправлено сладостей всего: {treatSended}
[!] Сколько раз был флуд контроль: {flood}
                         4 секунды ожидания""")

        response = post('https://api.vk.com/method/apps.incrementFriendScore', data={
            'api_id': 7968630,
            'method': 'apps.incrementFriendScore',
            'format': 'json',
            'v': 5.131,
            'access_token': access_token,
            'user_id': user,
            'request_id': 'incrementFriendScore'
        }).json()
        sleep(1)

        if response.get('response'):
            treat += 1
            treatSended += 1

        elif response.get('error'):

            if response['error']['error_code'] == 1:
                treatSended += 1

            elif response['error']['error_code'] == 9:
                flood += 1
                sleep(4)
        else:
            print(response)


def main():

    access_token = input('Токен, пжалста: ')
    print('[?]Получение списка друзей')
    users = getFriends(access_token)
    try:
        if users[0] != "":
            print('  [!]Список получен')
        else:
            print('пиздец какой-то произошел...')
            system('exit')
        print('  [>]Отправка сладостей...')
        sendTreat(users, access_token)
    except AttributeError:
        pass
    except TypeError:
        pass


if __name__ == '__main__':
    main()
