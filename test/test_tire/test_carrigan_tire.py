import unittest

from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_need_service_true(self):
        tire_worns = [0.9,0.9,0.7,0.5,0.8]
        tire = CarriganTire(tire_worns)
        self.assertTrue(tire.need_service())
    
    def test_need_service_false(self):
        tire_worns = [0.8,0.7,0.6,0.5]
        tire = CarriganTire(tire_worns)
        self.assertFalse(tire.need_service())