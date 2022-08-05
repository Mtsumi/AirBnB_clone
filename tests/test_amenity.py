import unittest
from models.amenity import Amenity

class test_Amenity(unittest.TestCase):

    def setUp(self):
        """Executed before each test"""
        self.a1 = Amenity("Has washing machine")
        #self.a1.save()
        #a1.name = "Has washing machine"
    
    def tearDown(self):
        """Executed after each test"""
        pass

    def test_Amenityname(self):
        self.assertEqual(self.a1.name, "Has washing machine")
