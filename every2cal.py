# -*- coding: utf8 -*-
import getpass
import everytime
import argparse
from convert import Convert

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--xml", type=str, help="Location of timetable xml file", required=False)
    parser.add_argument("--begin", type=str, help="Semester beginning date", required=True)
    parser.add_argument("--end", type=str, help="Semester ending date", required=True)
    args = parser.parse_args()

    xml = ""
    if (args.xml):
        xml = args.xml

    else:
        username = input('에브리타임 아이디 : ')
        password = getpass.getpass()

        year = input('가져올 년도 : ')
        semester = input('가져올 학기 : ')

        e = everytime.Everytime(username, password)
        xml = e.get_timetable(year, semester)

    c = Convert(xml)
    c.get_calendar(c.get_subjects(), args.begin, args.end)


def DownCal(begin, end, username, password):

    # year = input('가져올 년도 : ')
    # semester = input('가져올 학기 : ')

    e = everytime.Everytime(username, password)
    xml = e.get_timetable(year, semester)

    c = Convert(xml)
    c.get_calendar(c.get_subjects(), begin, end)

    print('test SUCESS')


if __name__ == '__main__':
    main()