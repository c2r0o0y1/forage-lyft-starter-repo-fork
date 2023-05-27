from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spinder_battery import SpinderBattery

from car import Car

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpinderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_is_on) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpinderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car


    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
