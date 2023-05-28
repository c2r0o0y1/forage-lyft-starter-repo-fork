from servicable import Servicable


class Car(Servicable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def need_service(self):
        return self.engine.need_service() or self.battery.need_service() or self.tire.need_service()