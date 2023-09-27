class Animal:
    
    def __init__(self):
        self.age = 0 # 전역변수 초기화

    def go1year(self):        
        self.age += 1
    
class Human(Animal): # 상속 받을때는 괄호안에 부모클래스 넣으면 됨
    def __init__(self):
        super().__init__() # 자바는 컴파일때 super를 생성허지만 파이썬은 컴파일언어가 아니라 조상을 호출해야함 
        self.nation = "korea"
    
    def immigration(self, nation):
        self.nation = nation
        
if __name__ == '__main__':
            
    ani = Animal()
    print("00", ani.age)
    ani.go1year()
    print("00", ani.age)
    
    hum = Human()
    print(hum.nation)
    print(hum.age)
    hum.immigration("america")
    hum.go1year()
    print(hum.nation)
    print(hum.age)


    