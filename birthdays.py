from datetime import datetime, timedelta


users = [
    {"name": "Bill", "birthday": datetime(year=1989, month=12, day=18)},
    {"name": "Ivan", "birthday": datetime(year=1985, month=12, day=23)},
    {"name": "Petro", "birthday": datetime(year=1992, month=12, day=17)},
    {"name": "Alisa", "birthday": datetime(year=1995, month=12, day=18)},
    {"name": "Bob", "birthday": datetime(year=1987, month=12, day=20)},
    {"name": "Anna", "birthday": datetime(year=1999, month=12, day=22)},
    {"name": "Kim", "birthday": datetime(year=1990, month=12, day=22)},
    {"name": "Marina", "birthday": datetime(year=1995, month=12, day=23)},
    {"name": "Sofia", "birthday": datetime(year=1993, month=12, day=25)},
    {"name": "Iryna", "birthday": datetime(year=1988, month=12, day=20)},
]


def get_birthdays_per_week(users):
    current_date = datetime.now().date()
    next_week_monday = (
        current_date - timedelta(days=current_date.weekday()) + timedelta(weeks=1)
    )
    start_period = (
        current_date - timedelta(days=current_date.weekday()) + timedelta(days=5)
    )
    end_period = start_period + timedelta(days=6)
    birthdays = {}
    for user in users:
        # if current_date.month == user['birthday'].month: # Можуть бути помилки, якщо викличемо при зміні місяців
        current_bd = user["birthday"].replace(year=current_date.year).date()
        if start_period <= current_bd <= end_period:
            if current_bd.weekday() in (5, 6):
                current_bd = next_week_monday
            if birthdays.get(current_bd):
                birthdays[current_bd].append(user["name"])
            else:
                birthdays[current_bd] = [user["name"]]

    return dict(sorted(birthdays.items()))
    #         if user['birthday'].day in [next_week_monday.day, next_week_monday.day-1, next_week_monday.day-2]:
    #             birthdays['Monday'].append(user['name'])
    #         elif user['birthday'].day == next_week_monday.day + 1:
    #             birthdays['Tuesday'].append(user['name'])
    #         elif user['birthday'].day == next_week_monday.day + 2:
    #             birthdays['Wednesday'].append(user['name'])
    #         elif user['birthday'].day == next_week_monday.day + 3:
    #             birthdays['Thursday'].append(user['name'])
    #         elif user['birthday'].day == next_week_monday.day + 4:
    #             birthdays['Friday'].append(user['name'])
    # for day in birthdays:
    #     if len(birthdays[day]) > 0:
    #         a = ', '.join(birthdays[day])
    #         print(f'{day}: {a}')


if __name__ == "__main__":
    bds = get_birthdays_per_week(users)
    for dt, users in bds.items():
        print(f'{dt.strftime("%A")} : {", ".join(users)}')
