print("hello, my name is Hiếu and these are my sheep sizes")
size = [5, 7, 300, 90, 24, 50, 75]
print(size)
n = max(size)
print("Now my biggest sheep has size", n, "let's shear it")
size[size.index(n)]=8
print("After shearing, here is my flock: ")
print(size)
for i in range(len(size)):
    size[i] = size[i] + 50
print("One month is passed, now here is my flock: ")
print(size)


