"""
Created on Sat Jun  3 22:53:07 2023
coding: utf-8

"""

def alph2num(alphabets):
    result = []
    alph_list=[chr(ord('A')+i) for i in range(26)]
    alph_list+=[' ','?','!']
    for alph in alphabets:
        result.append(alph_list.index(alph))
    return result

def num2alph(numbers):
    result = ""
    alph=[chr(ord('A')+i) for i in range(26)]
    alph+=[' ','?','!']
    for num in numbers:
        result+=alph[num]
    return result
if __name__=="__main__":

    r=num2alph([0,1,2,3])
    r=alph2num('CAT')
    print(r)
    