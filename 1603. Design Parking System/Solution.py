# -*- coding: utf-8 -*-
class ParkingSystem(object):
    # Runtime 96 ms / Memory 13.8 MB
    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType):
        if (carType==1 and self.big>0):
            self.big -= 1
            return True
        elif (carType==2 and self.medium>0):
            self.medium -= 1
            return True
        elif (carType==3 and self.small>0):
            self.small -= 1
            return True
        else:
            return False
        


    # Runtime 99 ms / Memory 13.7 MB
    def __init__(self, big, medium, small):
        self.space = defaultdict(int)
        self.space[1] = big
        self.space[2] = medium
        self.space[3] = small
        

    def addCar(self, carType):
        if (self.space[carType]>0):
            self.space[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)2],cost[-1])