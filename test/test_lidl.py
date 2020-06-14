import os
import unittest

from lidl_receipts_de import Lidl

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR, "data"
)


def get_filepath(filename):
    return os.path.join(DATA_DIR, filename)


class TestLidl(unittest.TestCase):

    def check(self, filename, price, _date):
        lidl = Lidl()
        file_path = get_filepath(filename)

        self.assertTrue(
            lidl.identify(file_path)
        )

        result = lidl.extract(file_path)

        self.assertEqual(
            result['simple_keys']['price'], price
        )

        self.assertEqual(
            result['simple_keys']['date'], _date
        )

    def test_lidl_1(self):
        self.check(
            "lidl-1.hocr",
            price='39,68',
            _date='04.05,20'
        )

    def test_lidl_2(self):

        self.check(
            "lidl-2.hocr",
            price='42,82',
            _date='06,05.20'
        )

    def test_lidl_3(self):

        self.check(
            "lidl-3.hocr",
            price='32,74',
            _date='27.04,20'
        )

    def test_lidl_4(self):

        self.check(
            "lidl-4.hocr",
            price='37.77',
            _date='29.04.20'
        )

    def test_lidl_5(self):

        self.check(
            "lidl-5.hocr",
            price='23.99',
            _date='24,04,20'
        )

    def test_lidl_8(self):

        self.check(
            "lidl-8.hocr",
            price='29,64',
            _date='20.04,20'
        )
