h = float(input("bạn cao bao nhiêu cm ? :"))
w = float(input("bạn nặng bao nhiêu kg ? :"))
m = 0.01 * h
bmi = w / ( m * m)
print("chi so BMI của bạn là : ",bmi)
if bmi < 16:
    print("Giảm cân (severely) ")
elif bmi < 18.5:
    print("Thiếu cân (underweight)")
elif bmi < 25:
    print("Bình Thường (normal")
elif bmi < 30:
    print("thừa cân (overweight) ")
else:
    print("béo phì (obese)")
