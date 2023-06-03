"""
Created on Sat Jun  3 22:53:07 2023
coding: utf-8

"""

def alph2num(alphabets):
    numbers = []
    for alphabet in alphabets:
        if 'A' <= alphabet <= 'Z':
            number = ord(alphabet) - 64
            numbers.append(number)
        else:
            numbers.append(0)
    return numbers

def num2alph(numbers):
    alphabets = ""
    for number in numbers:
        if 1 <= number <= 26:
            alphabet = chr(number + 64)
            alphabets += alphabet
        else:
            alphabets += " "
    return alphabets
if __name__=="__main__":
    alph='NOMONEYY'
    r=alph2num(alph)
    print(r)