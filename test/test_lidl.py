import os
import re
import unittest

from hocron import Hocron, LinePattern

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR, "data"
)


def get_hocr(category, filename):
    hocr = Hocron(
        os.path.join(DATA_DIR, filename)
    )
    return hocr


class TestLidl(unittest.TestCase):

    def test_lidl_1(self):

        hocr = get_hocr("lidl-1.hocr")

        line_pattern = LinePattern(
            ['EUR', re.compile('\d+[\.,]\d\d$')]
        )  # noqa
        value = hocr.get_labeled_value(line_pattern)

        self.assertTrue(value)
        self.assertEqual(value, '41,92')
