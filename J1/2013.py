c1 = int(input("What is the age of the youngest child? "))
c2 = int(input("What is the age of the middle child? "))
c3 = 0

if c1 <= 0 or c1 > 50:
    print("Error, input an age between 1 and 50");
elif c2 < c1 or c2 >50:
    print("Error, input an age between 1 and 50");
else:
    print(str((c2 - c1) + c2));
    
