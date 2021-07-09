"""Module for testing functions of main.py"""


import pytest
from freezegun import freeze_time
from main import even_odd, sum_all, time_of_day


@pytest.mark.parametrize('num, expected', [
    (0, 'even'),
    (1, 'odd'),
    (-1, 'odd'),
    (2, 'even'),
])
def test_even_odd(num, expected):
    """Testing values around zero"""
    assert even_odd(num) == expected


@pytest.mark.parametrize('nums, expected', [
    ([1, 2, 3, -1, -2, -3], 0),
    ([1.0, 2.0, 3.0, -1.0, -2.0, -3.0], 0),
    ([1, 2, 3, 4, 5], 15),
    ([5], 5),
])
def test_sum_all(nums, expected):
    """Testing floats and ints, one element list """
    assert sum_all(*nums) == expected


def test_time_of_day():
    """Testing using freeze_time lib to avoid mock problem"""
    with freeze_time("2012-01-14 1:00:01"):
        assert time_of_day() == 'night'

    with freeze_time("2012-01-14 10:00:01"):
        assert time_of_day() == 'morning'

    with freeze_time("2012-01-14 13:00:01"):
        assert time_of_day() == 'afternoon'

    with freeze_time("2012-01-14 20:00:01"):
        assert time_of_day() == 'night'
