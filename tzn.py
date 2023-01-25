import datetime
import pytz

def get_time_in_zone(zone):
    tz = pytz.timezone(zone)
    current_time = datetime.datetime.now(tz)
    return current_time.strftime("%H:%M:%S %Z %z")

zone = input("Enter a time zone (e.g. 'Europe/London'): ")
time = get_time_in_zone(zone)
print(f"The current time in {zone} is {time}.")
