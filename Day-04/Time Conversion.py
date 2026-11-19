def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    remaining = s[2:8]

    if period == "AM":
        if hour == 12:
            hour = 0

    else:
        if hour != 12:
            hour += 12

    return f"{hour:02d}{remaining}"
