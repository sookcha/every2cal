import everytime

__author__ = "Hoseong Son <me@sookcha.com>"

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
        path = input('경로 : ')

        e = everytime.Everytime(path)
        xml = e.get_timetable()

    c = Convert(xml)
    c.get_calendar(c.get_subjects(), args.begin, args.end)


if __name__ == '__main__':
    main()