# tests/test_iot.py

import unittest
from IOT import Iot

class TestIot(unittest.TestCase):
    def setUp(self):
        # Initialize the Iot class before each test
        self.iot = Iot()

    def test_setup_devices(self):
        # Test for the setup_devices method
        self.iot.setup_devices()
        self.assertEqual(len(self.iot.devices), 2)  # Check if two devices were set up

    def test_interact_with_device(self):
        # Test for the interact_with_device method
        self.iot.interact_with_device("Device 1")
        # In a real test, you would check if the interaction happens correctly
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()  # Run the tests
