from datetime import datetime, timedelta, timezone
import re
def to_timestamp(dt_str, tz_str):
    dt_str = input('please input your datetime info: ')
    tz_str = input('please input your timezone info: ')
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    hr = 
    set_dt = utc_dt.astimezone(timezone(timedelta(hours=)))
    cday = datetime.strptime(tinfo, %Y-%m-%d %)



if __name__ == "__main__":
    to_timestamp(dt_str, tz_str)
    print(cday)