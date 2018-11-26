a=float(input("nhap a :"))
b=float(input("nhap b :"))
c=float(input("nhap c :"))
a2 = a*2

if a==0:
    if b==0:
        if c==0:
            print("phuong trinh co vo so nghiem ")
        else:
            print("phuong trinh vo nghiem ")
    else:
        print("phuong co nghiem :",-c/b)
else:
    delta = b*b-4*a*c
    delta_sqrt = delta**0.5
    if delta < 0:
        print("phuong trinh vo nghiem")
    elif delta==0:
        print("phuong trinh co nghiem kep ",-b/(2*a))
    else:
        print("phuong trinh co hai nghiem phan biet")
        print("x1 = ",(-b + delta_sqrt)/(2*a))
        print("x2 = ",(-b - delta_sqrt)/(2*a))