print("Xin Chào ! Bạn hãy trả lời câu hỏi sau đại số sau đây :" )
print("nếu thay x = 8 vào biểu thức 4*(x+3) = ? ")
s = [35 , 36 , 40 , 44]

for i in range(len(s)):
    print(i+1,". ",s[i])
tl = int(input("hãy chon 1 trong 4 đáp án trên  ? "))
if tl == 4:
    print("bingo :D")
else:
    print(":(")
