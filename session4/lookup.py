teencode= {
    "aye": "anh yeu em",
    "nyc": "nguoi yeu cu ",
    "stt": "status",
    

}

# n=input("dac san cac tinh thanh :")
# print(dic[n])
# n=input("do you want to update ? ")
# if n == "yes":

# else:

#     print(":)")
while True:
    print(*teencode)
    code = input("your code ?")
    if code in teencode:
        print(teencode[code])
        print()
        update = input("do you want to update (Y/N)").upper()
        if update == "Y":
            new = input("your transalte:")
            teencode[code]=new
            print("Done")
    else:
        print("not found")
        create = input("do you want to contribute").upper()
        if create == "Y":
            translation = input("your translate?")