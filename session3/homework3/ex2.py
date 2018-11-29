my_number = 22
loop=True
while loop:
    your_number = int(input("Hi ! hãy đoán con số của tôi nào : "))
    if your_number == 22:
        print("Bingo :D ")
        loop=False
    elif your_number < 22:
        print("too small :(  ")
    else:
        print("A little too large :( ")
        