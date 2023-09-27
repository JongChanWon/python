# 첫수를 입력하시오 1
# 끝수를 입력하시오 5
# 1에서 5까지의 합은 15 입니다.

a = input("첫수를 입력하시오")
b = input("끝수를 입력하시오")

aa = int(a)
bb = int(b)

arr = list(range(aa, bb+1))

sum = 0
for i in arr:
    sum += i
print("{} 에서 {} 까지의 합은 {} 입니다".format(a,b,sum))