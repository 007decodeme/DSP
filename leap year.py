class Date:
     def __init__(self, d, m, y):
         self.d = d
         self.m = m
         self.y = y

     def day(myself):
         print("Day:",myself.d)

     def month(self):
         print("Month:", self.m)

     def year(self):
         print("Year:", self.y)

     def monthName(self):
         months = ["Unknown", "January", "February", "March", "April", "May", "June",
                  "July","August", "September", "October", "November", "December"]
         print("Month Name:", months[self.m])
     def isLeapYear(self):
         if (self.y % 400 == 0)or (self.y % 4 == 0 and self.y % 100 != 0):
             print("It is a Leap year")
         else:
             print("It is not a Leap year")


dd = int(input("Enter the day: "))
mm = int(input("Enter the month: "))
yy = int(input("Enter the year: "))


d1 = Date(dd, mm, yy)
d1.day()
d1.month()
d1.year()
d1.monthName()
d1.isLeapYear()
