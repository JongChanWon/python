# 홀/짝을 선택하시오 홀
# 나:홀
# 컴:짝
# 결과: 짐
from random import random

rnd = random()

result = ""
me = input("홀/짝을 선택하시오")

if 0.5 < rnd:
    com = "홀"
elif 0.5 > rnd:
    com = "짝"

if me == com:
    result = "승리"
else:
    result = "패배"
    
    
print("나: " + me)
print("컴: " + com)
print("결과: " + result)