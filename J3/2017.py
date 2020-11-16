#input
r = input()
s = input()
t = int(input())

b = r.split()
c = s.split()

b = list(map(int,b))
c = list(map(int,c))
for i in range (0,2):
    if b[i] > 1000 or b[i] > 1000:
        print("error")
    elif b[i] < -1000 or b[i] < -1000:
        print("error")
    if t > 10000 or t < 0:
        print("error")

startX = int(b[0])
startY = int(b[1])
endX = int(c[0])
endY = int(c[1])
horizontal = int(c[0]-b[0])
vertical = int(c[1] - b[1])

distance = int(horizontal + vertical)

if distance <= t and distance != ((t-distance)/2 == 1):
    print("Y")
else:
    print("N")

