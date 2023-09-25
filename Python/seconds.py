s = int(input("Enter number of seconds: "))

print(s, "seconds is:")
h = s // 3600 # Get quotient
s = s % 3600 # Get Remainder
print(h, "hours")

m = s // 60
s = s % 60
print(m, "minutes")
print("and",s,"seconds")
