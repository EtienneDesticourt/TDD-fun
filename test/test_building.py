import unittest
from app.Building import Building
from app.Character import Character

class BuildingTestCase(unittest.TestCase):

    def test_building_create_character_success(self):
        B = Building()
        B.position = (10, 10)
        CharModel = Character()
        CharModel.strength = 20
        B.CharacterModels["Test Model"] = CharModel
        Char = B.createCharacter("Test Model")
        assert Char.strength == CharModel.strength
        assert Char.position == B.position

    def test_building_create_character_failure(self):
        B = Building()
        CharModel = Character()
        B.CharacterModels["Test Model"] = CharModel
        self.assertRaises(KeyError, B.createCharacter, "Invalid Test Model")
