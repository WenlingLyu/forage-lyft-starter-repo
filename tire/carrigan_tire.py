
from tire.tire import Tire

class Carrigan_tire(Tire):
    def __init__(self, tires_one, tires_two, tires_three, tires_four):
        super().__init__()  
        self.tires_one = tires_one
        self.tires_two = tires_two
        self.tires_three = tires_three
        self.tires_four = tires_four
    
    def needs_service(self):
        if self.tires_one +  self.tires_two + self.tires_three + self.tires_four >= 3:
            return True
        else:
            return False
  