sum = 0

d11=int(input("Digit 11? "))
d12=int(input("Digit 12? "))
d13=int(input("Digit 13? "))


def sum1to3 (d11, d12, d13):
    sum = 9 *1 + 7 *3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3 + d11 * 1 + d12 * 3 + d13 * 1
    print ("The 1-3-sum is " + str(sum));

sum1to3 (d11, d12, d13)
