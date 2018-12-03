cmd = input("what do you want (c,r,u,d,e) ? ")
items = ["com","bun","pho"]
print(items)
while True:
    if cmd == "c":
        c = input("bạn muốn thêm gì : ")
        items.append(c)
        print(items)
    elif cmd == "r":
        for index,item in enumerate(items):
            print(index + 1 , item, sep=". ")
    elif cmd == "u":
        u = int(input("bạn muốn update vào vị trí thứ mấy "))
        i = input("nội dung muốn update : ")
        items[u-1]=i
        print(items)
    elif cmd == "d":
        d=int(input("bạn muốn xoá vị trí thứ mấy : "))
    
        items.pop(d - 1)
        print(items)
    elif cmd == "e":
        print("chữ bạn vừa nhập ko có trong 4 chữ : c , r , u ,d")
        break
