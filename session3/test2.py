# loop = True
# while loop:
#     psw=input("enter your password ")
#     if len(psw) >= 8:
#         if (not psw.islower()):
#             if(not psw.isupper()):
#                 loop=False
# print("psw ok ")
n = int(input("nhap n :"))
dem=0
while n>0:
    
    n=n/10
    dem=dem+1
print(dem)