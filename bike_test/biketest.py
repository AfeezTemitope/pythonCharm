import unittest
from bike import Bike


class TestBike(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()
        self.bike.turn_on()

    def test_that_bike_can_turn_on(self):
        self.assertTrue(self.bike.isOn)

    def test_that_bike_can_turn_off(self):
        self.bike.turn_off()
        self.assertFalse(self.bike.isOn)

    def test_that_bike_can_accelerate(self):
        self.bike.set_acceleration(22)
        self.bike.increase_by_gear()
        self.assertEqual(24, self.bike.get_acceleration())

    def test_that_bike_can_deccelerate(self):
        self.bike.set_acceleration(22)
        self.bike.decrease_by_gear()
        self.assertEqual(20, self.bike.get_acceleration())

    def test_that_bike_can_increase_by_gear1(self):
        self.bike.set_acceleration(22)
        self.bike.set_gear(1)
        self.bike.increase_by_gear()
        self.assertEqual(23, self.bike.get_acceleration())

    def test_that_bike_can_increase_by_gear2(self):
        self.bike.set_acceleration(22)
        self.bike.set_gear(2)
        self.bike.increase_by_gear()
        self.assertEqual(24, self.bike.get_acceleration())

    def test_that_bike_can_increase_by_gear3(self):
        self.bike.set_acceleration(22)
        self.bike.set_gear(3)
        self.bike.increase_by_gear()
        self.assertEqual(25, self.bike.get_acceleration())

    def test_that_bike_can_increase_by_gear4(self):
        self.bike.set_acceleration(22)
        self.bike.set_gear(4)
        self.bike.increase_by_gear()
        self.assertEqual(26, self.bike.get_acceleration())

    def test_that_bike_can_decrease_by_gear1(self):
        self.bike.set_acceleration(22)
        self.bike.set_gear(1)
        self.bike.decrease_by_gear()
        self.assertEqual(21, self.bike.get_acceleration())

    def test_that_bike_can_decrease_by_gear2(self):
        self.bike.set_acceleration(22)
        self.bike.set_gear(2)
        self.bike.decrease_by_gear()
        self.assertEqual(20, self.bike.get_acceleration())

    def test_that_bike_can_decrease_by_gear3(self):
        self.bike.set_acceleration(22)
        self.bike.set_gear(3)
        self.bike.decrease_by_gear()
        self.assertEqual(19, self.bike.get_acceleration())

    def test_that_bike_can_decrease_by_gear4(self):
        self.bike.set_acceleration(22)
        self.bike.set_gear(4)
        self.bike.decrease_by_gear()
        self.assertEqual(18, self.bike.get_acceleration())

    def test_gear_changes_with_acceleration(self):
        self.bike.turn_on()
        self.bike.set_acceleration(25)
        self.assertEqual(2, self.bike.get_gear())

if __name__ == '__main__':
    unittest.main()
