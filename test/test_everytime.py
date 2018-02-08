import unittest

from everytime import Everytime


class TestEveryTime(unittest.TestCase):
    def test_get_request(self):
        e = Everytime()
        print(e.get_timetable('', '', '2017', '1'))


if __name__ == '__main__':
    unittest.main()
