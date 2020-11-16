s = input()
d = s.split()

d = list(map(int,d))

c = [0]

for i in range(0,4):
    c.append(c[i] + d[i])

for i in range(0,5):
    r = []
    for x in range(0,5):
        distance = c[x] - c[i]
        if distance < 0:
            distance = distance * -1
        r.append(distance)
    print (*r)
    
