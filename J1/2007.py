x = int(input("Type in one of the weights: "))
y = int(input("Type in another weight: "))
z = int(input("Type in the last weight: "))

def putinorder(x,y,z):
    if x > y and x < z:
        print ("The Mama Bear's Bowl's weight is: " + str(x));
    elif x > z and x < y:
        print ("The Mama Bear's Bowl's weight is: " + str(x));
    elif y> z and y < x:
        print ("The Mama Bear's Bowl's weight is: " + str(y));
    elif y>x and y < z:
        print ("The Mama Bear's Bowl's weight is: " + str(y));
        
    if z > y and z < x:
        print ("The Mama Bear's Bowl's weight is: " + str(z));
    elif z > x and z < y:
        print ("The Mama Bear's Bowl's weight is: " + str(z));


putinorder (x,y,z)


