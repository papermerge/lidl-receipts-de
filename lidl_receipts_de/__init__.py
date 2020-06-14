import re

from hocron import Hocron, LinePattern


class Lidl:

    SIMPLE_KEYS = [
        'shop',
        'price',
        'date'
    ]

    COMP_KEY = []

    def extract(hocr_file_path):
        result = {
            'simple_keys': {
                'shop': 'lidl',
                'price': None,
                'date': None
            },
            'comp_key': []
        }
        hocr = Hocron(hocr_file_path)
        price_line_pattern = LinePattern(
            ['EUR', re.compile('\d+[\.,]+\d\d$')]  # noqa
        )
        date_line_pattern = LinePattern(
            ['Datum', re.compile('\d\d.\d\d.\d\d')]  # noqa
        )
        price = hocr.get_labeled_value(price_line_pattern)
        _date = hocr.get_labeled_value(date_line_pattern)

        result['simple_keys']['price'] = price
        result['simple_keys']['date'] = _date

        return result

    def identify(hocr_file_path):
        hocr = Hocron(hocr_file_path)
        first_word = hocr.first_word

        if not first_word:
            return False

        pattern = re.compile('L.D.$')

        return re.match(pattern, first_word)
