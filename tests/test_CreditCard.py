from check_personal_identity_number_and_credit_card.check_CreditCard import check_card

correct_credit_card = [
    "5903404081939887",
    "5647059750233243",
    "5895852773751707",
    "5076981967882548",
    "5951907718121621",
    "4343038115875419",
    "4831603000966794",
    "4297830589891898",
    "4837431421099738",
    "4643072406330674",
]
bad_credit_card = [
    "5903404081957887",
    "5647057750233243",
    "5895852777561707",
    "5076981964562548",
    "5951907234121621",
    "4343038567875419",
    "4831603876966794",
    "4297830678891898",
    "4837431345099738",
    "4643072435330674",
]


def test_credit_card():
    for i in correct_credit_card:
        assert check_card(i)
    for i in bad_credit_card:
        assert not check_card(i)