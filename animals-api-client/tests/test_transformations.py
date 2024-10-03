import unittest
from src.utils.transformations import transform_animal

class TestTransformations(unittest.TestCase):
    def test_transform_animal(self):
        animal = {"id": 1, "name": "Badger", "born_at": 1331031285051, "friends": "Wolf,Otter"}
        expected = {"id": 1, "name": "Badger", "born_at": "2012-03-06T11:34:45.051Z", "friends": ["Wolf", "Otter"]}
        self.assertEqual(transform_animal(animal), expected)

if __name__ == "__main__":
    unittest.main()