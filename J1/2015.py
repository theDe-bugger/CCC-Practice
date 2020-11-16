smonth = 2
sday = 18

month = int(input("What is the month? "))
day = int(input("What is the date? "))

if month > smonth and day > sday:
    print("After");
elif month < smonth and day < sday:
    print("Before");
elif month == smonth and day == sday:
    print("Special");
else:
    print("Error");
