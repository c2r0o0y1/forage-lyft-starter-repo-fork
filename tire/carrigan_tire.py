from .tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_worns):
        self.tire_worns = tire_worns

    def needs_services(self):
        counter = 0

        for i in self.tire_worns:
            if i >= 0.9:
                counter += 1
        
        if counter >= 1:
            return True
        else:
            False
