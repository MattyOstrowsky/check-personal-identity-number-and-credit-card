def pesel(pesel):
    pesel_list = list(str(pesel))

    if len(str(pesel)) != 11:
        return False
    else:
        try:
            int(pesel)

        except ValueError:
            return False

    control = int(pesel_list[0]) * 9 + int(pesel_list[1]) * 7 + int(pesel_list[2]) * 3 + int(pesel_list[3]) * 1 + int(pesel_list[4]) * 9 + int(pesel_list[5]) * 7 + int(pesel_list[6]) * 3 + int(pesel_list[7]) * 1 + int(pesel_list[8]) * 9 + int(pesel_list[9]) * 7

    if control % 10 != int(pesel_list[10]):
        return False

    if int(pesel_list[2]+pesel_list[3]) // 20 == 1:
        age = 2000
        mouth = int(pesel_list[2]+pesel_list[3])-20
    elif int(pesel_list[2]+pesel_list[3]) // 20 == 0:
        age = 1900
        mouth = int(pesel_list[2]+pesel_list[3])
    elif int(pesel_list[2]+pesel_list[3]) // 20 == 4:
        age = 1800
        mouth = int(pesel_list[2]+pesel_list[3])-80

    mouth_dict = {'1': "stycznia", '2': "lutego", '3': "marca", '4': "kwietnia", '5': "maja", '6': "czerwca", '7': "lipca", '8': "sierpnia", '9': "września", '10': "października", '11': "listopada", '12':"grudnia" }

    return print(pesel_list[4]+pesel_list[5], mouth_dict[str(mouth)], age+int(pesel_list[0]+pesel_list[1])), True


def check_card(num):
    if(len(num)) % 2 == 0:
        x =0
    else:
        x =1
    num_list = list(str(num))

    sum = 0
    for i in num_list:
        licznik = int(i)*(2 if x % 2 == 0 else 1)

        if licznik > 9:
            fast = list(str(licznik))
            licznik = int(fast[0])+int(fast[1])

        x += 1
        sum += licznik

    if sum % 10 ==0:
        return True
    else:
        return False


