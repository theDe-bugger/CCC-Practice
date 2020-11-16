x = int(input("What is the first angle? "))
y = int(input("What is the second angle? "))
z = int(input("What ist the third angle? "))

if x and y and z == 60:
    print("Equilateral Triangle");
elif x + y + z == 180 and x == y or x == z or y==z:
    print("Isosceles Triangle");
elif x + y + z == 180 and x!=y and x!=z:
    print("Scalene Triangle");
elif x + y + z == 180 and y!=x and y!=z:
    print("Scalene Triangle");
elif x + y + z == 180 and z!=y and z!=x:
    print("Scalene Triangle");
elif x + y + z != 180:
    print("Error");
    
