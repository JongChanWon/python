
from random import random

# 1~100 까지 숫자중에 com = 50 을 선택했으면(random)
# 1~100사이수 컴퓨터로 지정
# for문 10번 돌려서

# 숫자를 입력하세요
# 20을 입력했으면 20 up

# 숫자를 입력하세요
# 70을 입력했으면 70 down

# 숫자를 입력하세요
# 50을 입력했으면 50 정답입니다

com = int(random()* 100) + 1
print(com)
for i in range(10):
    mine = input('숫자를 입력하세요')
    imine = int(mine)
    if imine == com:
        print("{} 정답입니다.".format(mine))
        break
    elif imine > com:
        print("{} Down".format(mine))
    else:
        print("{} Up".format(mine))