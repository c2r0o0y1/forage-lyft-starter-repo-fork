import unittest
from datetime import datetime

from battery.spinder_battery import SpinderBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(current_date.year - 3)
        battery = SpinderBattery(current_date, last_service_date)
        self.assertTrue(battery.need_service())

    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(current_date.year - 1)
        battery = SpinderBattery(current_date, last_service_date)
        self.assertFalse(battery.need_service())