import calendar
weekdays = list(calendar.day_name[0:5])
weekends = list(calendar.day_name[5:7])
weekday_hours = "10am - 7pm"
weekend_hours = "9am - 5pm" 

# hours_of_operation = {
#     weekdays: weekday_hours,
#     weekends: weekday_hours
# }

# hours_of_operation = {
#     "Monday": weekday_hours,
#     "Saturday": weekend_hours
# }
hours_of_operation = {}
for day in weekdays:
    hours_of_operation[day] = weekday_hours
for day in weekends:
    hours_of_operation[day] = weekend_hours


# context = {}
# context["hours_of_operation"] = hours_of_operation

for k, v in hours_of_operation.items():
    print(f"k:{k} and v:{v}")