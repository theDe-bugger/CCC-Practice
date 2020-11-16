
N = int(input("Input value of N between 1 and 10000: "))

while N < 1 or N > 10000:
    N = int(input("Input value of N between 1 and 10000: "))

k = int(input("Input value of k between 1 and 5: "))

while 1 > k or k > 5:
    k = int(input("Input value of k between 1 and 5: "))

shiftysum = 0

if k == 1:
    shiftysum = N + (N * 10)
if k == 2:
    shiftysum = N + (N * 10) + (N * 100)
if k == 3:
    shiftysum = N + (N * 10) + (N * 100) + (N * 1000)
if k == 4:
    shiftysum = N + (N * 10) + (N * 100) + (N * 1000) + (N * 10000)
if k == 5:
    shiftysum = N + (N * 10) + (N * 100) + (N * 1000) + (N * 10000) + (N *100000)

print (str(shiftysum));
