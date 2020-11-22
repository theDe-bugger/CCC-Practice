s = int(input())
m = int(input())
l = int(input())

score = (s*1) + (m*2) + (l*3)

if score>=10:
    print("happy")
elif score<10:
    print("sad")