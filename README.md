# **Check personal identity and credit card number**

<img align="right" width="33%" src="https://img.icons8.com/external-justicon-lineal-color-justicon/452/external-wallet-ecommerce-justicon-lineal-color-justicon.png">

## Table of contents
* [General info](#general-info)
* [Installation](#installation)
* [How to run it](#how-to-run-it)
* [Basic usages](#basic-usages)
* [License](#license)


## General info

Simple CLI script to  check your date of birth and validate
personal identity or validate credit card number.
## Installation

1. Git clone repository:
```bash
$ git clone https://github.com/gunater/check-personal-identity-number-and-credit-card.git
```
2. Install the necessary python dependencies you can use `pipenv`:
```bash
$ pipenv install
$ piipenv shell
```
or you can install from requirements.txt with `pip`:
```bash
$ pip install -r requirements.txt
```
## How to run it
To run the script, go to the main directory:
```bash
$ cd check_personal_identity_number_and_credit_card/
```
and then run script with an argument `--help`:
```bash
$ python3 checker.py --help
```
## Basic usages
### 1. Identity number
to validate your identity number and check your date of birth, type with example identity number:
```bash
$ python3 checker.py pesel --p 53052486359
```
and script will return your date:
```text
24 maja 1953
```
if you need more information type:
```bash
$ python3 checker.py pesel --help
```
### 2. Credit card number
to validate your credit card number type:
```bash
$ python3 checker.py creditcard --n 4343038115875419
```
and script will return:
```text
The credit card number is correct!
```
if you need more information type:
```bash
$ python3 checker.py creditcard --help
```
## License
All code is licensed under an MIT license. This allows you to re-use the code freely, remixed in both commercial and non-commercial projects. The only requirement is to include the same license when distributing.
