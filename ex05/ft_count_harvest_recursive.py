def ft_count_harvest_recursive():
    days = int(input("Days until the harvest: "))
    _count_days(1, days)


def _count_days(day, days):
    if day > days:
        print("Harvest time!")
        return
    print("Day", day)
    _count_days(day + 1, days)
    
