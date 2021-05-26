from datetime import datetime, timedelta

# dt = datetime(2021,5,26, 9,10,45)
# add_dt = dt + timedelta(days=5)
# print(add_dt)

# exercise
today = datetime.today()
print(today)

for i in range(1,10):
    two_weeks_apart = today + timedelta(days=14)
    today = two_weeks_apart
    print(two_weeks_apart.strftime("%Y-%M-%D"))