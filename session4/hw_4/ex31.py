from random import randint
#chọn random trong list :
words = ["champion","meticulous","hexagon"]

n = randint(0,len(words)-1)
k = list(words[n])

#giống bài 3 
for _ in range(len(k)):
     j = randint(0,len(k)-1)
     ch = k[j]
     print(ch,end = " ")
     k.pop(j)
print() 
h = str(input("your answer:"))
if h == words[n]:
    print("mãi iu :D")
else:
    print(":(")