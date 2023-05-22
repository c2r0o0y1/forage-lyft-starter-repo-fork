from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spinder_battery import SpinderBattery

from car import Car

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        pass

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        pass

    def create_palindrome(self,current_date, last_service_date, warning_light_on) -> Car:
        pass

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        pass

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        pass
