line = str(input("Please input the line: "))

while len(line) > 255 or len(line) < 1:
    line = str(input("Please input the line between 1 and 255 characters: "))

happy = line.count(":-)")
sad = line.count(":-(")

if happy == 0 and sad == 0:
    print ("none")
elif happy == sad:
    print ("unsure")
elif happy > sad:
    print ("happy")
else:
    print ("sad")

