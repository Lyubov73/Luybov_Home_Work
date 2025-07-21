def mont_to_season(month):
    if month in(12,1,2):
        return"Зима"
    elif month in(3,4,5):
        return"Весна"
    elif month in(6,7,8):
        return"Лето"
    elif month in(9,10,11):
        return"Осень"
    else:
        return"Некорректный номер месяца"
    print(mont_to_season(2))
    print(mont_to_season(5))
    print(mont_to_season(8))
    print(mont_to_season(10))
    print(mont_to_season(13))