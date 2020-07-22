import re

from hocron import Hocron, LinePattern


class Lidl:

    SIMPLE_KEYS = [
        'shop',
        'price',
        'date'
    ]

    def extract(self, hocr):
        result = {
            'simple_keys': {
                'shop': 'lidl',
                'price': None,
                'date': None
            },
            'comp_key': []
        }
        # hocron module is a thin layer of API for HOCR format
        # processing
        hocr = Hocron(hocr)

        price_line_pattern_1 = LinePattern(
            ['EUR', re.compile('\d+[\.,]+\d\d$')]  # noqa
        )
        price_line_pattern_2 = LinePattern(
            ['EUR', re.compile('\d+$')]  # noqa
        )
        date_line_pattern_1 = LinePattern(
            ['Datum', re.compile('\d\d.\d\d.\d\d')]  # noqa
        )
        date_line_pattern_2 = LinePattern(
            ['Datum.', re.compile('\d\d.\d\d.\d\d')]  # noqa
        )
        price_1 = hocr.get_labeled_value(price_line_pattern_1)
        price_2 = hocr.get_labeled_value(price_line_pattern_2)
        _date_1 = hocr.get_labeled_value(date_line_pattern_1)
        _date_2 = hocr.get_labeled_value(date_line_pattern_2)

        # in future there will be 'comp keys', that's why
        # it is a good idea to keep a separate namespace
        result['simple_keys']['price'] = price_1 or price_2
        result['simple_keys']['date'] = _date_1 or _date_2

        return result
