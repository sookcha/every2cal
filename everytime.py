import requests
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
            session.post(url, data=payload)

            timetable_result = session.post("https://api.everytime.kr/find/timetable/table/list/semester", data={
                "semester": semester,
                "year": year
            })

            tree = ElementTree.fromstring(timetable_result.text)
            for target in tree.findall('table[@is_primary="1"]'):
                id = target.get('id')
                table_xml = session.post("https://api.everytime.kr/find/timetable/table", data={
                    "id": id
                })
                result_xml = table_xml.text
        return result_xml