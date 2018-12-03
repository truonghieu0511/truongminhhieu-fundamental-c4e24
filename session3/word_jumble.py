from random import randint
word = "hexagon"
characters = list(word)
print(characters)
for _ in range(len(characters)):
    # 1 chọn ra 1 chữ cái ngẫu nhiên
    # 1.1  random => number => len-1
    # 1.2 number => index
    i=randint(0,len(characters)-1)
    ch=characters[i]
    # 2 in ra 
    print(ch,end=" ")
    # 3 xoá nó đi 
    characters.pop(i)
print()
user_guess = input("your guess ? :")
if user_guess == word:
    print("hura")
else:
    print(":(")