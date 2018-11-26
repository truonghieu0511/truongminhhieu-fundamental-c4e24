yob = int(input("your year of birth ? "))
age = 2018 - yob
print(age)

if age < 10:
    print("Baby")
elif age < 18:
    print("teenage")
else:
    print("adult")