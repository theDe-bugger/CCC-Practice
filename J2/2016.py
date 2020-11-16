separator = ' '
list1 = map(int, raw_input("Enter the first line:").split(separator))
list2 = map(int, raw_input("Enter the second line:").split(separator))
list3 = map(int, raw_input("Enter the third line:").split(separator))
list4 = map(int, raw_input("Enter the fourth line:").split(separator))

a = sum(list1)
b = sum(list2)
c = sum(list3)
d = sum(list4)

a1 = sum (list1[0], list2[0], list3[0], list4[0])
b1 = sum (list1[1], list2[1], list3[1], list4[1])
c1 = sum (list1[2], list2[2], list3[2], list4[2])
d1 = sum (list1[3], list2[3], list3[3], list4[3])

values = [a,b,c,d,a1,b1,c1,d1]
if all( v == values[0] for v in values):
    print("Magic Square");
else:
    print("False");
