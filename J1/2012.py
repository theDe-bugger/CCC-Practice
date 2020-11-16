F = 0

slimit = int(input("Enter the speed limit: "))
rspeed = int(input("Enter the recorded speed of the car: "))

if rspeed > slimit and rspeed < slimit + 30:
    print("You are speeding and your fine is $100");
elif rspeed > slimit + 21 and rspeed <= slimit + 30:
    print("You are speeding and your fine is $270");
elif rspeed > slimit + 31:
    print("You are speeding and your fine is $500");
elif rspeed < slimit:
    print("Congratulations, you are within the speed limit.");
elif rspeed <= 0:
    print("Ivalid, put in a valid speed for the car");
elif slimit <= 0:
    print("Ivalid, put in a valid speed limit");
