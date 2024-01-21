import calendar;

numbers=[1,2,3,4,5,6,7,8,9,10,11,12]

print ("HERE IS THE CALENDAR :")
print(" ")

for num in numbers:
    cal = calendar.month(2024, num)
    print(num)
    print(cal)
