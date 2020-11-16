from typing import List
t = 0
x = 0
y = 0
onepress = 'adgjmptw'
twopress = 'behknqux'
threepress = 'cfilorvy'
fourpress = 'sz'

one = 'abc'
two = 'def'
three = 'ghi'
four ='jkl'
five = 'mno'
six ='pqrs'
seven ='tuv'
eight ='wxyz'
time= []
s = str(input())
if s!= "halt" and len(s) < 20:
    if len(s) == 1:
        for i in range(1, len(s) + 1):
            t = 0
            if s[x] in onepress:
                t = t + 1
                x = x + 1
            elif s[x] in twopress:
                t = t + 2
                x = x + 1
            elif s[x] in threepress:
                t = t + 3
                x = x + 1
            elif s[x] in fourpress:
                t = t + 4
                x = x + 1
        time.append(t)
    elif len(s) > 1:
        for i in range(1, len(s)):
            t = 0
            if s[x] in onepress:
                t = t + 1
                x = x + 1
            elif s[x] in twopress:
                t = t + 2
                x = x + 1
            elif s[x] in threepress:
                t = t + 3
                x = x + 1
            elif s[x] in fourpress:
                t = t + 4
                x = x + 1
        time.append(t)

while s!= "halt" and len(s) < 20:
    s = str(input())
    x = 0
    if len(s) == 1:
        for n in range (1,len(s)):
            t = 0
            if s[x] in onepress:
                t = t + 1
                x = x + 1
            elif s[x] in twopress:
                t = t + 2
                x = x + 1
            elif s[x] in threepress:
                t = t + 3
                x = x + 1
            elif s[x] in fourpress:
                t = t + 4
                x = x + 1
        time.append(t)
    elif len(s) > 1:
        for i in range(1, len(s)):
            t = 0
            if s[x] in onepress:
                t = t + 1
                x = x + 1
            elif s[x] in twopress:
                t = t + 2
                x = x + 1
            elif s[x] in threepress:
                t = t + 3
                x = x + 1
            elif s[x] in fourpress:
                t = t + 4
                x = x + 1
        time.append(t)


print (time);


