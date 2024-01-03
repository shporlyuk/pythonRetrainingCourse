from exceptions.exceptions import *


def to_minutes(hour):
    if not isinstance(hour, int) or hour < 0:
        raise InvalidHourException("Invalid input for hours.")
    return int(hour * 60)


def to_hours(minute):
    if not isinstance(minute, (int, float)) or minute < 0:
        raise InvalidMinuteException("Invalid input for minutes")
    return round(minute / 60, 4)


def is_whole_div(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise InvalidInputError("Invalid input.")
    if num2 == 0:
        raise InvalidDivisionException("Division by 0 error.")
    return num1 % num2 == 0