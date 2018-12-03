from random import randint


words = "champion"
chars = list(words)

for _ in range(len(chars)):
    i = randint(0, len(chars) - 1)
    ch = chars[i]

    print(ch, end=" ")

    chars.pop(i)

print()

n = input("Your guess? ")
if n == words:
    print("mãi iu :) ")
else:
    print(":(")
