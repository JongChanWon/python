class Mansuru:
    def __init__(self):
        self.money = 2400
        self.cnt_building = 10
    
    def buyBuilding(self, money):
        self.cnt_building += money
        self.money -= money
    

class Putin:
    def __init__(self):
        self.cnt_nuclear = 10000
    def war(self):
        self.cnt_nuclear -= 1


class Trump:
    def __init__(self):
        self.cnt_employee = 2000
    def youFire(self):
        self.cnt_employee -= 10
        
class YoungNam(Mansuru, Putin, Trump):
    def __init__(self):
        super().__init__()
        
        Mansuru.__init__(self)
        Putin.__init__(self)
        Trump.__init__(self)
    
if __name__ == '__main__':
    yn = YoungNam()
    
    print(yn.money)
    print(yn.cnt_building)
    yn.buyBuilding(100)
    print(yn.money)
    print(yn.cnt_building)
    
    print(yn.cnt_nuclear)
    for i in range(10):
        yn.war()
    print(yn.cnt_nuclear)
    
    print(yn.cnt_employee)
    yn.youFire()
    print(yn.cnt_employee)
        
        
    """   
        ma = Mansuru()
        print(ma.cnt_building)
        print(ma.money)
        ma.buyBuilding(30)
        print(ma.cnt_building)
        print(ma.money)
        
        pu = Putin()
        print(pu.cnt_nuclear)
        pu.war()
        print(pu.cnt_nuclear)
        
        tr = Trump()
        print(tr.cnt_employee)
        tr.youFire()
        print(tr.cnt_employee)
        
    """
    
    
    
    