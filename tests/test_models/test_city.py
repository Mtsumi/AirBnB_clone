import unittest
from models.city import City

class test_Amenity(unittest.TestCase):

    def setUp(self):
        """Executed before each test"""
        self.c1 = City("001", "Mombasa")
    
    def tearDown(self):
        """Executed after each test"""
        pass

    def test_Cityname(self):
        self.assertEqual(self.c1.state_id, "001")
        self.assertEqual(self.c1.name, "Mombasa")
