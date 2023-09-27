# 1에서 부터 10까지의 합을 구하시오

arr = list(range(1, 10+1))
print(arr)
a = sum(arr) # sum 함수
print(a)

_sum = 0
for i in arr:
    _sum += i
print(_sum)