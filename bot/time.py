from pytz import timezone
import datetime


def get_moscow_datetime():
    spb_timezone = timezone("Europe/Moscow")
    local_time = datetime.datetime.now()
    current_time = local_time.astimezone(spb_timezone)
    return current_time
