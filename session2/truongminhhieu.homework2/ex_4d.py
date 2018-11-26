import sys 
n = int(input("nhập n : " ))
for i in range(1,n,2):
     sys.stdout.write(" x ")
     sys.stdout.write(" * ")
  
if n % 2 !=0:    
     print("x")