duration = int(input("Seconds: "))
second = 0
minute = 0
hour = 0
day = 0

if duration < 60:
    second = duration
elif duration >= 60 and duration < 3600:
    seconds = duration % 60
    if seconds != 0:
        second = seconds
    minute = (duration - seconds) // 60
elif duration >= 3600 and duration < 86400:
    seconds = duration % 3600
    hour = (duration - seconds) // 3600
    if seconds != 0:
        second = seconds % 60
        minute = (seconds - second) // 60
elif duration > 86400:
    seconds = duration % 86400
    second = seconds % 60
    remainder_hour = seconds % 3600
    hour = (seconds - remainder_hour) // 3600
    minute = remainder_hour // 60
    day = (duration - seconds) // 86400

print(f'days: {day}, hour: {hour}, minute: {minute}, seconds:{second}')
