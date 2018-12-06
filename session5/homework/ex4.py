question= {
   "If x = 8, then what is the value of 4(x + 3) ?" : [30,31,32,44],
   "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?" : ["about 55","about 65","about 75","about 85"],
}

answer= {
   "If x = 8, then what is the value of 4(x + 3) ?":  4,
   "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?" : 2,
}
s=0

for i in question:
    print(i)
    for key,value in enumerate(question[i],1):
        print(key,value,sep=". ")
    n = int(input("your choice : "))
    if n == answer[i]:
        print("bingo ! ")
        s = s + 1
    else:
        print(":(")

print("Your correct answer:", s , "out of", len(question), "question!" )
