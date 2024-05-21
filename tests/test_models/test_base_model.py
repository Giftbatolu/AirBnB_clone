#!/usr/bin/python3

"""
    tests the BaseModel through unit testing.

"""

import unittest
from datetime import datetime
from models. base_model BaseModel
from models.engine import file_storage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up a variable to store the instance for all tests."""
        self.bm_obj = BaseModel()

    def test_base_initialization(self):
        """Test if the BaseModel has the correct initial attributes."""
        self.assertTrue(hasattr(self.bm_obj, "id"))
        self.assertTrue(hasattr(self.bm_obj, "created_at"))
        self.assertTrue(hasattr(self.bm_obj, "updated_at"))

    def test_the_str_method(self):
        """Test the str method of BaseModel."""
        expected_str_representation = (
            f"[{type(self.bm_obj).__name__}] ({self.bm_obj.id}) "
            f"{self.bm_obj.__dict__}"
        )
        actual_str_rep = str(self.bm_obj)
        self.assertEqual(expected_str_representation, actual_str_rep)

    def test_save_method(self):
        """GTest if the save method updates the updated_at attribute."""
        original_updated_at = self.bm_obj.updated_at
        self.bm_obj.save()
        self.assertNotEqual(original_updated_at, self.bm_obj.updated_at)

    def test_object_type(self):
        """Test if the attributes are of the correct type."""
        self.assertIsInstance(self.bm_obj.created_at, datetime)
        self.assertIsInstance(self.bm_obj.updated_at, datetime)
        self.assertIsInstance(self.bm_obj.id, str)

    def test_two_instances_have_unique_id(self):
        """Test if two instances of BaseModel have unique ids."""
        bm_obj2 = BaseModel()
        self.assertNotEqual(self.bm_obj.id, bm_obj2.id)

    def test_init_with_kwargs(self):
        """Test initialization of BaseModel with keyword arguments."""
        kwargs = {
            'id': 'test_id',
            'created_at': '2024-05-17T02:55:09.636825',
            'updated_at': '2024-05-17T02:55:09.636825',
            'name': 'Test',
            'number': 123,
        }
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.id, 'test_id')
        self.assertEqual(bm.created_at, datetime.strptime(
            kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm.updated_at, datetime.strptime(
            kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm.name, 'Test')
        self.assertEqual(bm.number, 123)

    def test_init_with_invalid_datetime(self):
        """ Test initialization of BaseModel with invalid
        datetime strings raises ValueError."""

        kwargs = {
            'id': 'test_id',
            'created_at': 'invalid_datetime',
            'updated_at': 'invalid_datetime',
        }
        with self.assertRaises(ValueError):
            BaseModel(**kwargs)


if __name__ == "__main__":
    unittest.main()
