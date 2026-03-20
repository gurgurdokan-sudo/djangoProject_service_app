import calendar
import datetime
import jpholiday

def get_month_days(year, month):
    cal = calendar.monthcalendar(year, month)
    days = []

    for week in cal:
        for day in week:
            if day == 0:
                continue

            date = datetime.date(year, month, day)
            days.append({
                "day": day,
                "weekday": date.weekday(),  
                "weekday_jp": "月火水木金土日"[date.weekday()],
                "is_sun": date.weekday() == 6,
                "is_sat": date.weekday() == 5,
                "is_holiday": jpholiday.is_holiday(date),
                "holiday_name": jpholiday.is_holiday_name(date),
            })
    return days
