# -*- coding: utf8 -*-
__author__ = "Hoseong Son <me@sookcha.com>"

import argparse

from convert import Convert

parser = argparse.ArgumentParser()
parser.add_argument("--xml", type=str, help="Location of timetable xml file", required=True)
parser.add_argument("--begin", type=str, help="Semester beginning date", required=True)
parser.add_argument("--end", type=str, help="Semester ending date", required=True)
args = parser.parse_args()

c = Convert(args.xml)
c.get_calendar(c.get_subjects(), args.begin, args.end)
