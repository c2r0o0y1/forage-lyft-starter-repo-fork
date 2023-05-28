from .tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_worns):
        self.tire_worns = tire_worns

    def needs_services(self):
        sum = 0
        for i in self.tire_worns:
            sum += i
        return sum >= 3
