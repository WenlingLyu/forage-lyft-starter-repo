
from tire.tire import Tire

class Octoprime_tire(Tire):
    def __init__(self, tires_one, tires_two, tires_three, tires_four):
        super().__init__()  
        self.tires_one = tires_one
        self.tires_two = tires_two
        self.tires_three = tires_three
        self.tires_four = tires_four
    
    def needs_service(self):
        if self.tires_one >= 0.9 or self.tires_two >= 0.9 or self.tires_three >= 0.9 or self.tires_four >= 0.9:
            return True
        else:
            return False
  
