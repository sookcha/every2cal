import requests

class Everytime:
    def get_request(self, userid, password, year, semester):
        payload = {'userid': userid, 'password': password}
        url = 'https://everytime.kr/user/login'

        with requests.Session() as s:
            r = s.post(url, data=payload)
            cookie = {'PHPSESSID': requests.utils.dict_from_cookiejar(s.cookies)['PHPSESSID']}
            print(cookie)