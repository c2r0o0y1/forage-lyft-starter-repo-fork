from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spinder_battery import SpinderBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_worns) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpinderBattery(last_service_date, current_date)
        if tire_type.lower() == 'carrigan':
            tire = CarriganTire(tire_worns)
        else:
            tire = OctoprimeTire(tire_worns)
        car = Car(engine, battery,tire)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_worns) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpinderBattery(current_date, last_service_date)
        if tire_type.lower() == 'carrigan':
            tire = CarriganTire(tire_worns)
        else:
            tire = OctoprimeTire(tire_worns)
        car = Car(engine, battery,tire)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_type, tire_worns) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpinderBattery(current_date, last_service_date)
        if tire_type.lower() == 'carrigan':
            tire = CarriganTire(tire_worns)
        else:
            tire = OctoprimeTire(tire_worns)
        car = Car(engine, battery,tire)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_worns) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        if tire_type.lower() == 'carrigan':
            tire = CarriganTire(tire_worns)
        else:
            tire = OctoprimeTire(tire_worns)
        car = Car(engine, battery,tire)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_worns) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        if tire_type.lower() == 'carrigan':
            tire = CarriganTire(tire_worns)
        else:
            tire = OctoprimeTire(tire_worns)
        car = Car(engine, battery,tire)
        return car
