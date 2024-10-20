import unittest
import re
import ipaddress

class Challenge(unittest.TestCase):

    def setUp(self):

    # wrong variable input to test if fail
        self.location = "Wrong_Location"  
        self.ip_address = "999.999.999.999"  
        self.subnet_mask = "256.256.256.256"  
        self.mac_address = "ZZ:ZZ:ZZ:ZZ:ZZ:ZZ"  
        self.device_type = "invalid_device"  
        self.prefix_length = 24
    # Correct Variables to test
        # self.location = "TIP_Manila"
        # self.ip_address = "192.168.45.25"
        # self.subnet_mask = "255.255.255.0"
        # self.mac_address = "00:1A:2B:3C:4D:5E"  
        # self.device_type = "PC"  
        # self.prefix_length = 24

    def test_location_and_ip(self):
        expected_location = "TIP_Manila"
        expected_ip = "192.168.45.25"
        expected_subnet_mask = "255.255.255.0"

        self.assertEqual(self.location, expected_location, f"Expected location '{expected_location}', got '{self.location}'")
        self.assertEqual(self.ip_address, expected_ip, f"Expected IP '{expected_ip}', got '{self.ip_address}'")
        self.assertEqual(self.subnet_mask, expected_subnet_mask, f"Expected subnet mask '{expected_subnet_mask}', got '{self.subnet_mask}'")

    def test_ip_address_format(self):
        pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        self.assertRegex(self.ip_address, pattern, f"IP address '{self.ip_address}' is not in valid format")

    def test_mac_address_format(self):
    
        pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        self.assertRegex(self.mac_address, pattern, f"MAC address '{self.mac_address}' is not in valid format")
    def test_device_type(self):
        valid_device_types = ['router', 'PC', 'switch', 'server']
        self.assertIn(self.device_type, valid_device_types, f"'{self.device_type}' is not a valid device type")

    def test_subnet_mask_correctness(self):
        expected_subnet_mask = ipaddress.IPv4Network(f'0.0.0.0/{self.prefix_length}').netmask
        self.assertEqual(self.subnet_mask, str(expected_subnet_mask),
                         f"Expected subnet mask '{expected_subnet_mask}', got '{self.subnet_mask}'")

if __name__ == "__main__":
    unittest.main()
