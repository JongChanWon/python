from random import random
def getHJ():
    rnd = random()
    
    ret = "홀"
    if rnd < 0.5:
        ret = "짝"
    return ret

com = getHJ()
print("com", com)