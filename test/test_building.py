import unittest

class BuildingTestCase(unittest.TestCase):

    def test_building_create_character_success(self):
        B = Building()
        CharModel = Character()
        CharModel.speed = 10
        CharModel.strength = 20
        B.CharacterModels["Test Model"] = CharModel
        Char = B.createCharacter("Test Model")
        assert Char.speed == CharModel.speed
        assert Char.strength == CharModel.strength
        assert Char.position == Building.position

    def test_building_create_character_failure(self):
        B = Building()
        CharModel = Character()
        CharModel.speed = 10
        CharModel.strength = 20
        B.CharacterModels["Test Model"] = CharModel
        self.assertRaises("KeyError", B.createCharacter, "Other Test Model")
