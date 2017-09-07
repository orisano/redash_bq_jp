# coding: utf-8
import re

import six

JAPANESE_COLUMN_MATCHER = re.compile(six.u("(?<=\\sas|\\sAs|\\saS|\\sAS)\\s+\\S*[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+[^\\s,;]*"))


def find_include_japanese_column(query):
    return [col.lstrip() for col in JAPANESE_COLUMN_MATCHER.findall(query)]

