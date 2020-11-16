import math

x = int(input("Input the x coordinate: "))
y = int(input("Input the y coordinate: "))

        
if x == 0 or x > 1000 or x < -1000:
    print ("Try another x coordinate")
  
elif y == 0 or y > 1000 or y < -1000:
    print ("Try another y coordinate")

else:
    if x > 0 and y > 0:
        print ("Quadrant 1");
    if x < 0 and y < 0:
        print ("Quadrant 3");
    if x < 0 and y > 0:
        print ("Quadrant 2");
    if x > 0 and y < 0:
        print ("Quadrant 4");
