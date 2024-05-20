""" This module tests the base model through unit testing """
#!/usr/bin/python3

from models.base_model import BaseModel
from datetime import datetime
import unittest

class Test_base_mode(unittest.TestCase):
    def setUp(self):
        """ to set a varible to store the instance for all at once"""
        self.bm_obj = BaseModel()

    def test_base_intalization(self):
        #bm_obj = BaseModel()
        # hasattrbut returns true if the attribute is present
        self.assertTrue(hasattr(self.bm_obj, "id"))
        self.assertTrue(hasattr(self.bm_obj, "created_at"))
        self.assertTrue(hasattr(self.bm_obj, "updated_at"))

    def test_the_str_method(self):
        #bm_obj = BaseModel()
        # commparing the expected and actual str
        expected_str_represenation = (
                f"[{type(self.bm_obj).__name__}] ({self.bm_obj.id}) {self.bm_obj.__dict__}")
        actual_str_rep = str(self.bm_obj)
        self.assertEqual(expected_str_represenation, actual_str_rep)

    def test_save_method(self):
        """ tests if the time given on updated_at is update with this mtd"""
        #self.bm_obj = BaseModel()
        orginal_updated_at = self.bm_obj.updated_at
        save_updated_time = self.bm_obj.save()
        self.assertNotEqual(orginal_updated_at, save_updated_time)
    
    def test_object_type(self):
        self.assertIsInstance(self.bm_obj.created_at, datetime) 
        self.assertIsInstance(self.bm_obj.updated_at, datetime) 
        self.assertIsInstance(self.bm_obj.id, str)
    
    def test_2_instances_have_unique_id(self):
        bm_obj2 = BaseModel()
        self.assertNotEqual(self.bm_obj.id, bm_obj2.id)

    def test_init_with_kwargs(self):
        """ Test initialization of BaseModel with keyword arguments """
        kwargs = {
            'id': 'test_id',
            'created_at': '2024-05-17T02:55:09.636825',
            'updated_at': '2024-05-17T02:55:09.636825',
            'name': 'Test',
            'number': 123
            }
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.id, 'test_id')
        self.assertEqual(bm.created_at, datetime(2024, 5, 17, 2, 55, 9, 636825))
        self.assertEqual(bm.updated_at, datetime(2024, 5, 17, 2, 55, 9, 636825))
        self.assertEqual(bm.name, 'Test')
        self.assertEqual(bm.number, 123)

    def test_init_with_invalid_datetime(self):
        """ Test initialization of BaseModel with invalid datetime strings """
        kwargs = { 
            'id': 'test_id',
            'created_at': 'invalid_datetime',
            'updated_at': 'invalid_datetime'
            }
        with self.assertRaises(ValueError):
            bm = BaseModel(**kwargs)

if __name__ == "__name__":
    unittest.main()

