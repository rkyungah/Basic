#응용 BMI 판정
weight = float(input("체중(kg)은 ? "))
height = float(input("키(cm)는 ? "))
## float == 실수형, int == 정수형

height = height / 100
bmi = weight / (height * height)

# BMI 값에 따라 결과로 분기
result = ""
if bmi < 18.5 :
    result = '마름'
if (bmi >= 18.5) and (bmi < 25) :
    result = '보통'
if (bmi >= 25) and (bmi <30) :
    result = '가벼운 비만'
if bmi >= 30 :
    result = '심한 비만'

print('-'*50)
print('BMI: ', bmi)
print('판정: ', result)
