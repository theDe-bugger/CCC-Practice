a = int(input("How many steps does Nikky walk forward? "))
b = int(input("How many steps does Nikky walk backward? "))
c = int(input("How many steps does Byron walk forward? "))
d = int(input("How many steps does Byron walk backward? "))
s = int(input("After how many steps does the teacher blow the whistle? "))

nikkySteps = 0
nikkyDistance = 0
next1 = a
x=1

while nikkySteps + next1 < s:
    nikkySteps = nikkySteps + next1;
    nikkyDistance = nikkyDistance + x * next1;
    if x == 1:
        next1 = b;
    else:
        next1 = a;
    x = x * -1

nikkyDistance = nikkyDistance + x * (s-nikkySteps);

byronSteps = 0
byronDistance = 0
next2 = c
y = 1

while byronSteps + next2 < s:
    byronSteps = byronSteps + next2;
    byronDistance = byronDistance + y * next2;
    if y == 1:
        next2 = d;
    else:
        next2 = c;
    y = y * -1;

byronDistance = byronDistance + y * (s-byronSteps);

if nikkyDistance > byronDistance:
    print ("Nikky");
elif nikkyDistance < byronDistance:
    print ("Byron");
else:
    print ("Tied");
    
