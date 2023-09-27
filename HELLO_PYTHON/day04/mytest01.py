# for i in range(2, 9+1):
#     for j in range(2, 9+1):
#         if i % 9 == 0 or i % 7 == 0:
#             print(f"{i} * {j} = {i*j}")
#
#     print("")
#

def showDan(dan):
    print("{} * {} = {}".format(dan, 1, dan * 1))
    print("{} * {} = {}".format(dan, 2, dan * 2))
    print("{} * {} = {}".format(dan, 3, dan * 3))
    print("{} * {} = {}".format(dan, 4, dan * 4))
    print("{} * {} = {}".format(dan, 5, dan * 5))
    print("{} * {} = {}".format(dan, 6, dan * 6))
    print("{} * {} = {}".format(dan, 7, dan * 7))
    print("{} * {} = {}".format(dan, 8, dan * 8))
    print("{} * {} = {}".format(dan, 9, dan * 9))
    
showDan(9)
showDan(6)
showDan(7)
showDan(3)
