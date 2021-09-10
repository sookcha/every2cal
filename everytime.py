from datetime import time
import requests
class Everytime:
    def __init__(self, path):
        self.path = path

    def get_timetable(self):
        return requests.post(
            "https://api.everytime.kr/find/timetable/table/friend",
            data={
                "identifier": self.path,
                "friendInfo": 'true'
            },
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "api.everytime.kr",
                "Origin": "https://everytime.kr",
                "Referer": "https://everytime.kr/",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
            }).text
