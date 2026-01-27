def ft_count_harvest_recursive(day=1, days=None):
    if days is None:
        days = int(input("Days until harvest: "))
    if day > days:
        print("Harvest time!")
        return
    print("Day", day)

    ft_count_harvest_recursive(day + 1, days)

#another version
def ft_count_harvest_recursive(day, days):
    if day > days:
        print("Harvest time!")
        return
    print("Day", day)
    ft_count_harvest_recursive(day + 1, days)


days = int(input("Days until the harvest: "))
ft_count_harvest_recursive(1, days)


