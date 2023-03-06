print("Hello, This Program will change the \
time from a 12 hour format to a 24 hour format.\n")

h = input("Enter current hour\n")
m = input("Enter current minute\n")
a = input("Enter 1 for AM or 2 for PM\n")

hour = int(h)
minute = int(m)
ap = int(a)
ampm = ""

if ap == 1:
    ampm = "AM"
if ap == 2 :
    ampm = "PM"

print("The time of day in a 12 hour format:\n")
print("{:02}".format(hour),":","{:02}".format(minute)," ",ampm,"\n")

print("The time of day in a 24 hour format:\n")

if ap == 2 :
    hour = hour+12

print("{:02}".format(hour),":","{:02}".format(minute),"\n")