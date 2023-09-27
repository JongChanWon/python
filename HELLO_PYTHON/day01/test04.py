# 첫수를 입력하시오 7
# 두번째 수를 입력하시오 8
# 7 은 8보다 작다
# 9 는 8보다 크다
# 6은 6과 같다

a = input("첫수를 입력하시오")
b = input("두번째 수를 입력하시오")

aa = int(a)
bb = int(b)

if aa < bb :
    print("{}은 {}보다 작다".format(a,b))
elif a > b :
    print(a + "는" + b + "보다 크다")
else:
    print(a + "은" + b + "과 같다")