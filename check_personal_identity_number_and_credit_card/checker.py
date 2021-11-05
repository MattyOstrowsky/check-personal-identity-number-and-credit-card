import click

from check_Pesel import pesel
from check_CreditCard import check_card


# Command Group
@click.group(name='main')
def cli_tools():
    """Tool related commands"""
    pass


@cli_tools.command(name='pesel', help='Check your pesel number')
@click.option('--p', default='53052486359', help='pesel number')
def option1(p):
    date, correct =pesel(p)
    if correct:
        return print(date)
    else:
        return print('pesel number incorrect!')


@cli_tools.command(name='creditcard', help='check your credit card number is correct')
@click.option('--n', default='4343038115875419', help='credit card number')
def search_cmd(n):
    answer = check_card(n)
    if answer:
        print('The credit card number is correct!')
    else:
        print('The credit card number is incorrect!')


if __name__ == '__main__':
    cli_tools()
