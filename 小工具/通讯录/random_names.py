#! python3
# -*- coding: utf-8 -*-
import os
import random
import string

current_dir=os.getcwd()
print("current_dir:",current_dir)
address_book_dir=os.path.join(current_dir,'小工具','通讯录')
print("address_book_dir:",address_book_dir)

FirstNames    = os.path.join(address_book_dir,'Names','FirstNames.txt')
MiddleNames   = os.path.join(address_book_dir,'Names','MiddleNames.txt')
LastNames     = os.path.join(address_book_dir,'Names','LastNames.txt')
CountyNames   = os.path.join(address_book_dir,'Names','CountyNames.txt')
PlaceNames    = os.path.join(address_book_dir,'Names','PlaceNames.txt')
StateNames    = os.path.join(address_book_dir,'Names','StateNames.txt')
CountryNames  = os.path.join(address_book_dir,'Names','CountryNames.txt')
CompanyNames  = os.path.join(address_book_dir,'Names','CompanyNames.txt')



def Number(start=0, end=100000):
    """
    Returns random integer between range of numbers
    """
    return random.randint(start, end)


def UpperChars(NoOfChars=2):
    """
    UpperChars(NoOfChars=2) Returns 2 random CAPITAL letters.
    """
    _char = ''
    for num in range(NoOfChars):
        _char += random.choice(string.ascii_uppercase)
    return _char


def rawCount(filename):
    """
    Function to get Line Count in txt files.
    rawcount('C:\A.txt') outputs integer value of count of lines.
    """
    print("filename:",filename)
    with open(filename, 'rb') as f:
        lines = 1
        buf_size = 1024 * 1024
        read_f = f.raw.read

        buf = read_f(buf_size)
        while buf:
            lines += buf.count(b'\n')
            buf = read_f(buf_size)
        return lines


def randomLine(filename):
    num = int(random.uniform(0, rawCount(filename)))
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            if i == num:
                break
    return line.strip('\n')


def First():
    return randomLine(FirstNames)


def Last():
    return randomLine(LastNames)


def Middle():
    return randomLine(MiddleNames)


def States():
    return randomLine(StateNames)


def Places():
    return randomLine(PlaceNames)


def County():
    return randomLine(CountyNames)


def Company():
    return randomLine(CompanyNames)


def Country():
    _Cc = randomLine(CountryNames)
    _Cc = _Cc.split('|')
    return _Cc[1]


def CountryCode():
    _Cc = randomLine(CountryNames)
    _Cc = _Cc.split('|')
    return _Cc[0]


def StateCode():
    return States().split(', ')[1]


def Full():
    """
    Returns a random First Name and Last Name combination
    """
    return ' '.join([First(), Last()])


def Address():
    """
    Returns a Random address in the Format:
    54F - Sauk, Middle, New Mexico, NM, 4292.
    """
    _door = str(Number(11, 99))
    _zip  = str(Number(1000, 9999))
    _adrs = ', '.join([Places(), County(), States(), _zip])
    _adrs = _door + UpperChars(1) + ' - ' + _adrs + '.'
    return _adrs


def ShortAddress():
    """
    Returns a Short Random address in the Format:
    31 Outagamie, Wisconsin, WI, 8281
    """
    _door = str(Number(11, 99))
    _zip  = str(Number(1000, 9999))
    _adrs = ', '.join([County(), States(), _zip])
    _adrs = _door + ' ' + _adrs
    return _adrs

def CreatePhone():
    for k in range(10):
        prelist=["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                 "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                 "186", "187", "188", "189"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))


if __name__ == '__main__':
    print(Full(), ' works at ', Company(), ' lives at ', Address(), StateCode(), Country())
