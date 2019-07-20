# -*- coding: utf-8 -*-

def rusngettext(number, forms):
    """Returns singular or plural text form of number."""
    if isinstance(forms, str):
        return forms

    first, second, third = forms

    result_from_100 = number % 100
    if result_from_100 < 10 or result_from_100 > 20:
        result_from_10 = number % 10
        if result_from_10 == 1:
            return first

        if 1 < result_from_10 < 5:
            return second

    return third
