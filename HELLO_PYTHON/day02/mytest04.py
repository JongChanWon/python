# 1~45까지의 수중에서 중복없이 6개의 수를 출력하세요
from random import random

#print(rnd.sample(arr, 6))
# arr = list(range(1, 6 + 1))

arr = list(range(1, 45+1))

# result = list(range(1, 6 + 1))

for i in range(1000):
    rnd = int(random()*45)
    a = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = a
print(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])