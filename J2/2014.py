

V = int(input("What is the total number of votes: "))


if 1 > V or V > 15:
   V = int(input("What is the total number of votes: "))

sequence = str(input("What is the order of votes: "))

if len(sequence) > V or len(sequence) < V:
    sequence = str(input("What is the order of votes: "))

acount = 0
for letter in sequence:
    if letter == "A":
        acount = acount + 1

bcount = V - acount


if acount == bcount:
    print("TIE");
elif acount > bcount:
    print ("A");
elif bcount > acount:
    print ("B");


            
        
