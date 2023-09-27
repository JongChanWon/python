# 랜덤함수를 이용하여 홀/짝을 출력하시오
# 0.5 > 홀
from random import random

rnd = random()

if 0.5 < rnd:
    print(str(rnd) + " (홀)")
elif 0.5 > rnd:
    print(str(rnd) + " (짝)")