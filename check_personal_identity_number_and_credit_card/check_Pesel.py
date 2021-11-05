def valid_pesel(pesel: str) -> bool:
    try:
        int(pesel)
    except ValueError:
        print("Pesel contains letters !")
        return False

    if len(str(pesel)) == 11:
        return True
    else:
        return False


def check_control_sum_pesel(pesel: str) -> bool:
    pesel_list = list(str(pesel))
    control = (
            int(pesel_list[0]) * 9
            + int(pesel_list[1]) * 7
            + int(pesel_list[2]) * 3
            + int(pesel_list[3]) * 1
            + int(pesel_list[4]) * 9
            + int(pesel_list[5]) * 7
            + int(pesel_list[6]) * 3
            + int(pesel_list[7]) * 1
            + int(pesel_list[8]) * 9
            + int(pesel_list[9]) * 7
    )
    if control % 10 != int(pesel_list[10]):
        return False
    else:
        return True


def check_age(pesel: str) -> (str, int):
    pesel_list = list(str(pesel))
    age = 0
    month = 0
    if int(pesel_list[2] + pesel_list[3]) // 20 == 1:
        age = 2000
        month = int(pesel_list[2] + pesel_list[3]) - 20
    elif int(pesel_list[2] + pesel_list[3]) // 20 == 0:
        age = 1900
        month = int(pesel_list[2] + pesel_list[3])
    elif int(pesel_list[2] + pesel_list[3]) // 20 == 4:
        age = 1800
        month = int(pesel_list[2] + pesel_list[3]) - 80
    return age, month


def dict_of_month() -> dict:
    return {
        "1": "stycznia",
        "2": "lutego",
        "3": "marca",
        "4": "kwietnia",
        "5": "maja",
        "6": "czerwca",
        "7": "lipca",
        "8": "sierpnia",
        "9": "września",
        "10": "października",
        "11": "listopada",
        "12": "grudnia",
    }


def pesel(pesel: str):
    if not valid_pesel(pesel) or not check_control_sum_pesel(pesel):
        return False
    else:
        pesel_list = list(str(pesel))
        age, mouth = check_age(pesel)
        month_dict = dict_of_month()
        date = (
                str(pesel_list[4] + pesel_list[5])
                + " "
                + str(month_dict[str(mouth)])
                + " "
                + str(age + int(pesel_list[0] + pesel_list[1]))
        )
        return date, True
