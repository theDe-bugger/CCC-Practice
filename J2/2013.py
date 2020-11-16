
word = str(input("Please input the word in all caps: "))

def Main():
    rotate = set("IOSHZXN")
    if set(word).issubset(rotate):
        print ("YES")
    else:
        print ("NO")

Main()
