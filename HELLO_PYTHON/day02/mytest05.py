# 가위 바위 보 를 입력하시오 가위
# 나: 가위
# com: 보
# 결과: 이김
from random import random

rnd = random()

result = ""
me = input("가위 바위 보 를 입력하시오")

if 0.5 < rnd:
    com = "가위"
elif 0.5 > rnd:
    com = "바위"
else:
    com = "보"
    
     
if me == com:
    result = "비김"
elif (me == "가위" and com == "바위") or (me == "바위" and com == "보") or (me == "보" and com == "가위"):
    result = "패배"
else:
    result = "승리"
    
    
print("나: " + me)
print("컴: " + com)
print("결과: " + result)