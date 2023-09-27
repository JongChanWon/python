def add_min_mul_div(a,b):
    return a+b, a-b, a*b, a/b

# sum, min, mul, div = add_min_mul_div(4,2)
min = add_min_mul_div(4,2)
# print("sum", sum)
print("min", min[0]) # 튜플... return의 0번째 1번째 2번재 가져올 수 있음
# print("mul", mul)
# print("div", div)