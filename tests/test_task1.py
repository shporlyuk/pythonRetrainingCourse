from tasks.task1 import *
import pytest


@pytest.mark.parametrize("hours, minutes", [(4, 240), (3.5, 210), (0, 0)])
def test_to_minutes(hours, minutes):
    assert to_minutes(hours) == minutes


@pytest.mark.parametrize("minutes, hours", [(90, 1.5), (75, 1.25), (0, 0)])
def test_to_hours(minutes, hours):
    assert to_hours(minutes) == hours


@pytest.mark.parametrize("num1, num2, expected", [(12, 3, True), (3, 2, False), (100, 5, True)])
def test_is_whole_div(num1, num2, expected):
    assert is_whole_div(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, exception", [(1, 0, InvalidDivisionException), ("g", 1, InvalidInputError)])
def test_is_whole_div_raises_exception(num1, num2, exception):
    with pytest.raises(exception):
        is_whole_div(num1, num2)