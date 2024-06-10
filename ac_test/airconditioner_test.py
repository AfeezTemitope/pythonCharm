import unittest

from AirConditioner import AirConditioner


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ac = AirConditioner()
        self.ac.turn_off()
    def test_that_ac_can_turn_on(self):
        self.ac.turn_on()
        self.assertTrue(self.ac.isOn)

    def test_that_ac_can_turn_off(self):
        self.assertFalse(self.ac.isOn)

    def test_to_set_temperature(self):
        self.ac.turn_on()
        self.ac.set_temperature(22)
        self.assertEqual(22, self.ac.get_temperature())

    def test_that_ac_can_increase(self):
        self.ac.turn_on()
        self.ac.set_temperature(22)
        self.ac.increase_temperature()
        self.assertEqual(23, self.ac.get_temperature())

    def test_that_ac_can_decrease(self):
        self.ac.turn_on()
        self.ac.set_temperature(22)
        self.ac.decrease_temperature()
        self.assertEqual(21,self.ac.get_temperature())

if __name__ == '__main__':
    unittest.main()
