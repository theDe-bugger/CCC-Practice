n = int(input())
lolx = []
loly = []
for i in range(n):
    x = input()
    sample = x.split(',')
    lolx.append(int(sample[0]))
    loly.append(int(sample[1]))

leftx = lolx[0]
rightx = lolx[0]
bottomy = loly[0]
topy = loly[0]

for y in range(len(lolx)):
    if lolx[y] < leftx:
        leftx = lolx[y] 
    elif lolx[y] > rightx:
        rightx = lolx[y]
    if loly[y] < bottomy:
        bottomy = loly[y] 
    elif loly[y] > topy:
        topy = loly[y]
print(str(leftx-1) + ',' + str(bottomy-1))
print(str(rightx+1) + ',' + str(topy+1))


