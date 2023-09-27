class Vehicle:
    def __init__(self): # 생성자
        print("constructor")
        self.cnt_wheel = 4
    
    def transformation(self, wheel):
        self.cnt_wheel = wheel
    
    def __del__(self): # 소멸자
        print("destroyer")
    
    def __str__(self):
        return "cnt_wheel:{}".format(self.cnt_wheel)
if __name__ == '__main__':
    veh = Vehicle()
    print(veh)
    veh.transformation(2)
    print(veh)
        