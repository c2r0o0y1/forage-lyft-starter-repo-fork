import unittest
from datetime import datetime

from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_car_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 35000
        last_service_mileage = 0

        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() == None)

    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())



class TestGlissade(unittest.TestCase):
    def test_car_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() == None)

    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())



class TestPalindrome(unittest.TestCase):
    def test_car_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service() == None)

    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())



class TestRorschach(unittest.TestCase):
    def test_car_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() == None)

    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

class TestThovex(unittest.TestCase):
    def test_car_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() == None)

    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
