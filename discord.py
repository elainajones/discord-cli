import requests
import json

import dotenv


class LoginSession:
    def __init__(self, login, password):
        self.url = 'https://discord.com/api/v9/auth/login'
        self.headers = {'Content-Type': 'application/json'}
        self.payload = {'login': login, 'password': password}

    def login(self):
        r = requests.post(
            self.url,
            headers=self.headers,
            json=self.payload,
        )

        if r.status_code == requests.codes.ok:
            r = json.loads(r.text)
        
            self.user_id = r['user_id']
            self.token = r['token']

            return True

        return False

class Requester:
    def __init__(self):
        pass
         
def main():
    config = dotenv.dotenv_values('.env')
    login = config['LOGIN']
    password = config['PASSWORD']

    session = LoginSession(login, password)
    session.login()
    
    headers = {'Content-Type': 'application/json', "Authorization": session.token}
    r = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    r = json.loads(r.text)
    
    for i in r:
        print(i["name"])
        print(i["id"])

if __name__ == '__main__':
    main()
