def count_day(duration):
    day = 0
    while duration >= 86400:
        day += 1
        duration = duration - 86400
    return day


def count_hour(duration):
    hour = 0
    while duration >= 3600:
        hour += 1
        duration = duration - 3600
    return hour


def count_minute(duration):
    minute = 0
    while duration >= 60:
        minute += 1
        duration = duration - 60
    return minute


def seconds_to_understandable_format(duration):
    day = 0
    hour = 0
    minute = 0
    second = 0
    if (duration >= 86400):
        remainder = duration % 86400
        duration -= remainder
        day = count_day(duration)
        duration = remainder
        if (duration >= 3600):
            remainder = duration % 3600
            duration -= remainder
            hour = count_day(duration)
            duration = remainder
            if (duration >= 60):
                remainder = duration % 60
                duration -= remainder
                minute = count_minute(duration)
                duration = remainder
                if duration < 60:
                    second = remainder
    print(f"{day} дней, {hour} часов, {minute} минуты, {second} секунды")


seconds = input('Количество секундов: ')
seconds_to_understandable_format(int(seconds))
