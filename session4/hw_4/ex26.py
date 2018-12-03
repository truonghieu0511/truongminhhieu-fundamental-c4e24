print("hello, my name is Hiếu and these are my sheep sizes")
size = [5, 7, 300, 90, 24, 50, 75]
print(size)
n = max(size)
print("Now my biggest sheep has size", n, "let's shear it")
size[size.index(n)]=8
print("After shearing, here is my flock: ")
print(size)
for i in range(2):
    print("MONTH", i + 1, ":")

    for i in range(len(size)):
        size[i] = int(size[i]) + 50
    print("One month has passed, now here is my flock: ")
    print(size)

    n = max(size)
    print("Now my biggest sheep has size", n, "let share it")

    size[size.index(n)] = 8
    print("After shearing, here is my flock: ")
    print(size)
print("MONTH 3 :")
for i in range(len(size)):
    size[i] = int(size[i])+50

print("One month has passed, now here is my flock: ")
print(size)

s = sum(size)
print("My flock in size total: ", s)
money = s * 2
print("I would get to: ", s, "* 2$ =", s * 2)