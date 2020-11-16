a = int(input("Please input reading 1: "))
b = int(input("Please input reading 2: "))
c = int(input("Please input reading 3: "))
d = int(input("Please input reading 4: "))

if a == b == c == d:
    print ("Constant Depth");
elif a > b > c > d:
    print ("Fish Diving");
elif a < b < c < d:
    print ("Fish Rising");
else:
    print ("No Fish");
