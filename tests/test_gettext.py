# -*- coding: utf-8 -*-
from collections import namedtuple
import pytest
from rusn import rusngettext

Forms = namedtuple('Forms', ('first', 'second', 'third'))

JAR = Forms('банка', 'банки', 'банок')


@pytest.mark.parametrize('number', [
    1, 101, 201, 301, 401, 501, 601, 701, 801, 901,
    21, 31, 41, 51, 61, 71, 81, 91,
    121, 131, 141, 151, 161, 171, 181, 191,
])
def test_first_jar_form(number):
    assert rusngettext(number, JAR) == JAR.first


@pytest.mark.parametrize('number', [
    2, 3, 4,
    22, 23, 24,
    102, 103, 104,
])
def test_second_jar_form(number):
    assert rusngettext(number, JAR) == JAR.second


@pytest.mark.parametrize('number', [
    5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    25, 26, 27, 28, 29, 105, 106, 107, 108, 109, 110, 111,
    112, 113, 114, 115, 116, 117, 118, 119, 120,
])
def test_second_jar_form(number):
    assert rusngettext(number, JAR) == JAR.third


@pytest.mark.parametrize('number', list(range(1, 40)))
def test_string_form(number):
    assert rusngettext(number, JAR.first) == JAR.first
    assert rusngettext(number, JAR.second) == JAR.second
    assert rusngettext(number, JAR.third) == JAR.third
