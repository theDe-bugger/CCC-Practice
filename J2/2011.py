h = int(input("Please input humidity factor: "))
M = int(input("Please input maximum number of hours Margaret will wait: "))

t = 1
A = (-6 * (t**4)) + (h * (t**3)) + (2 * t * t) + t


while t<M and A>0:
    t = t + 1
    A = (-6 * (t**4)) + (h * (t**3)) + (2 * t * t) + t
if A > 0:
    print ("The balloon does not touch the ground in the given time.");
else:
    print ("The balloon touches the ground at hour: \n" + t);
    
