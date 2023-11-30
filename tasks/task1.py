def to_minutes(hour):
    return int(hour * 60)


def to_hours(minute):
    return round(minute / 60, 4)


def is_whole_div(num1, num2):
    return num1 % num2 == 0