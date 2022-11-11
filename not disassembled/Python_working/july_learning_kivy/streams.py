import datetime
import variables


def podschet():
    year = int(variables.year)
    month = int(variables.month)
    day = int(variables.day)
    ostatok_hour = int(variables.hour)
    ostatok_minutes = int(variables.minutes)
    ostatok_seconds = int(variables.seconds)
    then = datetime.datetime(year, month, day, ostatok_hour, ostatok_minutes, ostatok_seconds)

    now = datetime.datetime.now()
    delta = now - then
    print("days: " + str(delta.days))
    hours = delta.seconds // 3600

    print("hours:" + str(hours))  # 186.0
    minutes = (delta.seconds % 3600) // 60
    print("minutes: " + str(minutes))  # 13.0
    seconds = (delta.seconds - ((hours * 3600) + (minutes * 60)))
    print("seconds: " + str(seconds))

    years = (delta.days // 365)
    month = (delta.days % 365) // 30

    if month <= 9:
        month = "0" + str(month)
    else:
        month = str(month)

    if years < 1:
        years = 0
    else:
        years = years

    if delta.days <= 9:
        days = "0" + str(delta.days)
    else:
        days = str(delta.days)
    if hours <= 9:
        hours = "0" + str(hours)
    else:
        hours = str(hours)
    if minutes <= 9:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)
    if seconds <= 9:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)

    itog = "Years:" + str(years) + ", " + "days:" + str(days) + ", " + "hours:" + str(hours) + ", " + "minutes:" + str(
        minutes) + ", " + "seconds:" + str(seconds)

    variables.value = itog


    return itog
