"""
Spyder Editor

This is a temporary script file.
"""
if __name__ == '__main__':
    s = input()
def show(true):
    if true==1:
        print("True")
    else:
        print("false")
def alphanum(s):
    true=0
    for i in s:
        if i.isalnum():
            true=1
    show(true)
def alpha(s):
    true=0
    for i in s:
        if i.isalpha():
            true=1
    show(true)
def dgt(s):
    true=0
    for i in s:
        if i.isdigit():
            true=1
    show(true)
def lower(s):
    true=0
    for i in s:
        if i.islower():
            true=1
    show(true)
def uper(s):
    true=0
    for i in s:
        if i.isupper():
            true=1
    show(true)
alphanum(s)
alpha(s)
dgt(s)
lower(s)
uper(s)                                   
          
