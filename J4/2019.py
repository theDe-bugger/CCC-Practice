x = [1,2]
y = [3,4]

s = str(input())
while len(s) > 1000000 or len(s) < 0:
    s = str(input())
for i in range(0,len(s)):
    if s[i] != 'H' and s[i] != 'V':
        s = str(input())

i = 0

for i in range(0,len(s)):
    if s[i] == 'V':
        x[0],x[1] = x[1],x[0]
        y[0],y[1] = y[1],y[0]
    elif s[i] == 'H':
        x[0],y[0] = y[0],x[0]
        x[1],y[1] = y[1],x[1]

print(str(x[0]) + ' ' + str(x[1]))
print(str(y[0]) + ' ' + str(y[1]))

