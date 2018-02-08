import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ElementTree

class Everytime:
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password

    def get_timetable(self, year, semester):
        result_xml = ""

        payload = {'userid': self.userid, 'password': self.password}
        url = 'https://everytime.kr/user/login'

        with requests.Session() as session:
            index_page_res = session.post(url, data=payload)

            soup = BeautifulSoup(index_page_res.text, 'html.parser')
            token = soup.find(id="userToken")["value"]

            timetable_result = session.post("http://timetable.everytime.kr/ajax/timetable/wizard/getTableList", data={
                "semester": semester,
                "year": year,
                "token": token
            })

            tree = ElementTree.fromstring(timetable_result.text)
            for target in tree.findall('table[@is_primary="1"]'):
                id = target.get('id')
                table_xml = session.post("http://timetable.everytime.kr/ajax/timetable/wizard/getOneTable", data={
                    "id": id,
                    "token": token
                })
                result_xml = table_xml


        return result_xml.text