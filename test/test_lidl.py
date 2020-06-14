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

    def test_lidl_1(self):

        lidl = Lidl()
        file_path = get_filepath("lidl-1.hocr")

        self.assertTrue(
            lidl.identify(file_path)
        )

        result = lidl.extract(file_path)

        self.assertEqual(
            result['simple_keys']['price'], '39,68'
        )

        self.assertEqual(
            result['simple_keys']['date'], '04.05,20'
        )
