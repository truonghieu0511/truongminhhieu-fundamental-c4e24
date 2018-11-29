loop=True
while loop:
    ps = input("password ? :")
    if len(ps) >= 8:
        if (not ps.islower()):
            if (not ps.isupper()):
                loop = False
            else:
                print("pass của bạn thiếu chữ thường")
        else:
            print("pass của bạn thiếu chữ hoa ") 
    else:
        print("pass của bạn phải nhiều hơn hoặc bằng 8 kí tự ")       
print("ok")
print(not ps.islower())