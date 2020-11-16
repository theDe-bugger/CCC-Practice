m = int(input("How many sides does the first die have? "))
n = int(input("How many sides does the second die have? "))

c = 0
if 1 > m > 1000 and 1 > n > 1000:
    print("Error");
        
else:
    for i in range(1, m+1):
        if 10 - i <= n and 10 - i > 0:
            c = c + 1
            i = i + 1
        elif 10 - i > n:
            c = c + 0

if c == 1:
    print("There is " + str(c) + " way to get the sum 10");
else:
    print("There are " + str(c) + " ways to get the sum 10");

