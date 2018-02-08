# -*- coding: utf8 -*-
__author__ = "Hoseong Son <me@sookcha.com>"

import unittest

from dateutil import parser

from convert import Convert


class TestConvert(unittest.TestCase):
    def test_get_subjects(self):
        c = Convert("table.xml")
        self.assertGreater(len(c.get_subjects()), 0)

    def test_get_calendar(self):
        c = Convert("table.xml")
        c.get_calendar(c.get_subjects(), "20180301", "20181231")

    def test_get_nearest_date(self):
        c = Convert("table.xml")
        self.assertEqual(c.get_nearest_date(start_date="20180301", weekday=4), parser.parse("20180302"))

if __name__ == '__main__':
    unittest.main()
