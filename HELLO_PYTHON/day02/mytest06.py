# 첫수를 입력하시오 1
# 끝수를 입력하시오 10
# 배수를 입력하시오 5
# 1 에서 10 까지의 5의 배수의 합은 15입니다

a = input("첫수를 입력하시오")
b = input("끝수를 입력하시오")
c = input("배수를 입력하시오")

aa = int(a)
bb = int(b)
cc = int(c)

arr = list(range(aa, bb + 1))
sum = 0

for i in arr:
    if i % cc == 0:
        sum += i
print("{} 에서 {} 까지의 {}배수의 합은 {} 입니다".format(a,b,c,sum))
