prices  = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}
total = 0
for pr in prices:
    print(pr,end=" ")
    print("price :" ,prices[pr])
    for st in stock:
        if pr == st:
            s = prices[pr] * stock[st]
            print(st," pr " ," * ",pr, "st"," = ",s )
            total = total + s
print("total = ",total)

            
print(total)

