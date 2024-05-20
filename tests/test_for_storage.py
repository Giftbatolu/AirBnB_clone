#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage("test_file.json")
        self.model = BaseModel()
        self.storage.new(self.model)

    def tearDown(self):
        """Clean up after the tests"""
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")
        self.storage._FileStorage__objects = {}

    def test_all(self):
        """Test that all returns the correct dictionary"""
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], self.model)

    def test_new(self):
        """Test that new adds an object to __objects"""
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.model)

    def test_save(self):
        """Test that save correctly serializes objects to JSON file"""
        self.storage.save()
        with open("test_file.json", "r") as file:
            content = json.load(file)
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, content)
        self.assertEqual(content[key]["id"], self.model.id)

    def test_reload(self):
        """Test that reload correctly deserializes JSON file to objects"""
        self.storage.save()
        new_storage = FileStorage("test_file.json")
        new_storage.reload()
        key = f"BaseModel.{self.model.id}"
        all_objects = new_storage.all()
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key].id, self.model.id)

    def test_reload_no_file(self):
        """Test that reload does nothing if file does not exist"""
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")
        new_storage = FileStorage("test_file.json")
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 0)

    def test_save_and_reload(self):
        """Test the complete save and reload cycle"""
        self.storage.save()
        new_storage = FileStorage("test_file.json")
        new_storage.reload()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, new_storage.all())
        self.assertEqual(new_storage.all()[key].id, self.model.id)

    def test_save_invalid_path(self):
        """Test saving to an invalid file path"""
        invalid_storage = FileStorage("/invalid_path/test_file.json")
        with self.assertRaises(OSError):
            invalid_storage.save()

    def Stest_reload_invalid_json(self):
        """Test reloading from an invalid JSON file"""
        with open("test_file.json", "w") as file:
            file.write("{ invalid json }")
        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()


if __name__ == "__main__":
    unittest.main()
