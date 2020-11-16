n = int(input())
while n >15 or n < 1:
    n = int(input())

antonia = 100
david = 100

for i in range(n):
    c = (input())
    lol = c.split()
    lol = list(map(int,lol))
    if lol[1] > lol[0]:
        antonia = antonia - lol[1]
    elif lol[0] > lol[1]:
        david = david - lol[0]
    elif lol[0] == lol[1]:
        david = david
        antonia = antonia
    lol = []


print(str(antonia))
print(str(david))
    
