import re

from hocron import Hocron


def identify(hocr_file_path):
    hocr = Hocron(hocr_file_path)
    first_word = hocr.first_word

    if not first_word:
        return False

    pattern = re.compile('L.D.$')

    return re.match(pattern, first_word)
