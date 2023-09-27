from day03.myoop01 import Animal

# 임포트 하는순간 전 클래스가 호출됨
# 메인메서드를 선언해야 그 전 메서드가 호출이 안됨
if __name__ == '__main__':
    
    ani = Animal()
    print("11", ani.age)
    ani.go1year()
    print("11", ani.age)