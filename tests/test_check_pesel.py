from check_personal_identity_number_and_credit_card.check_Pesel import (
    valid_pesel,
    check_control_sum_pesel,
    check_age,
    pesel,
)

correct_pesel = ["53052486359", "94120679457", "01240316649"]
too_long_pesel = "5305248635923"
too_short_pesel = "530524863"
with_letters_pesel = "530524d6a59"
bad_pesel = "53052486339"


class TestPesel:
    def test_valid_pesel(self):
        assert valid_pesel(too_long_pesel) == False
        assert not valid_pesel(too_short_pesel)
        assert not valid_pesel(with_letters_pesel)

    def test_check_sum(self):
        assert [check_control_sum_pesel(i) for i in correct_pesel]
        assert not check_control_sum_pesel(bad_pesel)

    def test_check_age(self):
        age, month = check_age(correct_pesel[0])
        assert age == 1900 and month == 5
        age, month = check_age(correct_pesel[1])
        assert age == 1900 and month == 12
        age, month = check_age(correct_pesel[2])
        assert age == 2000 and month == 4

    def test_pesel(self):
        date, check = pesel(correct_pesel[0])
        assert date == "24 maja 1953" and check
        date, check = pesel(correct_pesel[1])
        assert date == "06 grudnia 1994" and check
        date, check = pesel(correct_pesel[2])
        assert date == "03 kwietnia 2001" and check
