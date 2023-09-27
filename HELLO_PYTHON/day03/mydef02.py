def showDan(dan):
    print(str(dan) + "단")
    for i in range(1, 9+1):
        # print(dan, "*", i, "=", (dan*i))
        # print("{} * {} = {}".format(dan, i, dan * i))
        print(f"{dan} * {i} = {dan*i}")
showDan(6)