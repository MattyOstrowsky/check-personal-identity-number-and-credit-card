def check_card(num):
    if (len(num)) % 2 == 0:
        x = 0
    else:
        x = 1
    num_list = list(str(num))

    sum = 0
    for i in num_list:
        licznik = int(i) * (2 if x % 2 == 0 else 1)

        if licznik > 9:
            fast = list(str(licznik))
            licznik = int(fast[0]) + int(fast[1])

        x += 1
        sum += licznik

    if sum % 10 == 0:
        return True
    else:
        return False
