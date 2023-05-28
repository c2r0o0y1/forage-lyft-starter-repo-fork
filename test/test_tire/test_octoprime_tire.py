import unittest

from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_need_service_true(self):
        tire_worns = [0.8, 0.8, 0.8, 0.8]
        tire = OctoprimeTire(tire_worns)
        self.assertTrue(tire.need_service())
    
    def test_need_service_false(self):
        tire_worns = [0.6, 0.6, 0.6, 0.6]
        tire = OctoprimeTire(tire_worns)
        self.assertFalse(tire.need_service())