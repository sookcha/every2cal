# -*- coding: utf8 -*-
__author__ = "Hoseong Son <me@sookcha.com>"

import unittest

from dateutil import parser

from convert import Convert


class TestConvert(unittest.TestCase):
    test_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<response>'
        '<table id="111111" is_deleted="0" name="timetable" year="2017" semester="2" priv="0" primary="1" created_at="2017-01-01 00:00:00" updated_at="2017-01-01 00:00:00">'
        '<subject id="0000001">'
        '<name value="테스트 수업"/>'
        '<professor value="테스트 교수"/>'
        '<time value="수 F(16:30-17:45) [XX관X층X호실]&#xA;금 F(16:30-17:45) [XX관X층X호실]">'
        '<data day="2" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '<data day="4" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '</time>'
        '</subject>'
        '<subject id="0000002">'
        '<name value="테스트 수업"/>'
        '<professor value="테스트 교수"/>'
        '<time value="수 F(16:30-17:45) [XX관X층X호실]&#xA;금 F(16:30-17:45) [XX관X층X호실]">'
        '<data day="2" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '<data day="4" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '</time>'
        '</subject>'
        '<subject id="0000003">'
        '<name value="테스트 수업"/>'
        '<professor value="테스트 교수"/>'
        '<time value="수 F(16:30-17:45) [XX관X층X호실]&#xA;금 F(16:30-17:45) [XX관X층X호실]">'
        '<data day="2" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '<data day="4" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '</time>'
        '</subject>'
        '<subject id="0000004">'
        '<name value="테스트 수업"/>'
        '<professor value="테스트 교수"/>'
        '<time value="수 F(16:30-17:45) [XX관X층X호실]&#xA;금 F(16:30-17:45) [XX관X층X호실]">'
        '<data day="2" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '<data day="4" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '</time>'
        '</subject>'
        '<subject id="0000005">'
        '<name value="테스트 수업"/>'
        '<professor value="테스트 교수"/>'
        '<time value="수 F(16:30-17:45) [XX관X층X호실]&#xA;금 F(16:30-17:45) [XX관X층X호실]">'
        '<data day="2" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '<data day="4" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '</time>'
        '</subject>'
        '<subject id="0000006">'
        '<name value="테스트 수업"/>'
        '<professor value="테스트 교수"/>'
        '<time value="수 F(16:30-17:45) [XX관X층X호실]&#xA;금 F(16:30-17:45) [XX관X층X호실]">'
        '<data day="2" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '<data day="4" starttime="198" endtime="213" place="XX관X층X호실"/>'
        '</time>'
        '</subject>'
        '</table>'
        '</response>'
    )

    def test_get_subjects(self):
        c = Convert(self.test_xml)
        self.assertGreater(len(c.get_subjects()), 0)

    def test_get_calendar(self):
        c = Convert(self.test_xml)
        c.get_calendar(c.get_subjects(), "20180301", "20181231")

    def test_get_nearest_date(self):
        c = Convert(self.test_xml)
        self.assertEqual(c.get_nearest_date(start_date="20180301", weekday=4), parser.parse("20180302"))

if __name__ == '__main__':
    unittest.main()
