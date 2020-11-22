p = int(input())
n = int(input())
r = int(input())

newaffected = n
days = 0
total = n
while p >= total:
    newaffected = newaffected * r
    total += newaffected
    days +=1
print(days)