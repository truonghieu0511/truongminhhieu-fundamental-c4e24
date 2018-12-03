items = ["t-shirt","sweater"]
while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D) ? : ").upper()
    if n == "R":
        print("our items : ",end="")
        for i in range(len(items)):
            print(items[i],end=", ")
        print()  
    if n == "C":
        n_item = input("enter new item :")
        items.append(n_item)
        print("our items :" ,end="")
        print(items)
    if n == "U":
        vt = int(input("bạn muốn thêm sp vào vị trí thứ mấy ? "))
        n_item=input("new items : ")
        items[vt-1] = n_item
        print("our items :" ,end="")
        print(items)
    elif n == "D":
        del_vt = int(input("bạn muốn xoá sp ở vị trí nào ? "))
        items.pop(del_vt - 1)
        print(items)
    elif n == "E":
        break
              
   