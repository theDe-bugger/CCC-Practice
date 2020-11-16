
print("Welcome to Chip's Fast Food Emporium");

burger = int(input("Please enter a burger choice: "))
drink = int(input("Please enter a drink choice: "))
sideorder = int(input("Please enter a side order choice: "))
dessert = int(input("Please enter a desert choice: "))

totalCal = 0
if burger < 0 or burger > 4 or burger == 0:
    print("Not a valid choice, please chose from 1-4")

else:
        if burger == 1:
            totalCal= totalCal + 461;
        elif burger == 2:
            totalCal= totalCal + 431;
        elif burger == 3:
            totalCal= totalCal + 420;
        else:
            totalCal= totalCal + 0;
        

if drink < 0 or drink > 4 or drink == 0:
    print("Not a valid choice, please chose from 1-4")
else:
    if drink == 1:
        totalCal = totalCal + 130;
    elif drink == 2:
        totalCal= totalCal + 160;
    elif drink == 3:
        totalCal= totalCal + 118;
    else:
        totalCal= totalCal + 0;
    
    
if sideorder < 0 or sideorder > 4 or sideorder == 0:
    print("Not a valid choice, please chose from 1-4")
else:
    if sideorder == 1:
        totalCal= totalCal + 100;
    elif sideorder == 2:
        totalCal= totalCal + 57;
    elif sideorder == 3:
        totalCal= totalCal + 70;
    else:
        totalCal= totalCal + 0;
    
    
if dessert < 0 or dessert > 4 or dessert == 0:
    print("Not a valid choice, please chose from 1-4")
else:
    if dessert == 1:
        totalCal= totalCal + 167;
    elif dessert == 2:
        totalCal= totalCal + 266;
    elif dessert == 3:
        totalCal= totalCal + 75;
    elif dessert == 4:
        totalCal= totalCal + 0;

print ("The total calories is " + str(totalCal));




            
