consonants = 'bcdfghjklmnqrstvwxyz'
con1 = 'bc'
con2 = 'c'
con3 = 'dfg'
con4 = 'g'
con5 = 'hjkl'
con6 = 'l'
con7 = 'mnpqr'
con8 = 'r'
con9 = 'stvwxyz'
vowels = 'aeiou'
s = str(input())
c = str()
if len(s) > 30 or len(s) < 0:
    print ("Error")
else:
    for i in range(0,len(s)):
        c = c + s[i]
        if s[i] in con1:
            c = c + 'a'
        elif s[i] in con3:
            c = c + 'e'
        elif s[i] in con5:
            c = c + 'i'
        elif s[i] in con7:
            c = c + 'o'
        elif s[i] in con9:
            c = c + 'u'
        if s[i] in consonants:
            x = consonants.find(s[i])
            c = c + consonants[x+1]

print (c);
           
