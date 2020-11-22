t = str(input())
s = str(input())

sl = list(s)
tl = list(t)
count = 0

for i in range(len(tl)):

    for x in range(len(sl)):
        if (i+x)>len(tl):
            output = "no"
            break
        elif (i+x)<len(tl):
            if tl[i+x] in sl:
                output = "yes"
                sl.remove(tl[i+x])
                if sl == []:
                    output = "yes"
            else:
                sl = list(s)
                output = "no"
                break
print(output)



