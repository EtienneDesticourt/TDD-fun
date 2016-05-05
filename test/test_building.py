import unittest
from app.Building import Building
from app.Character import Character
from pygame import Rect as Zone

class BuildingTestCase(unittest.TestCase):

    def test_building_create_character_success(self):
        Building1 = Building(life = 10, affiliation = 0, Zone = Zone((10, 10), (1, 1)))
        CharModel = Character(strength = 10, life = 10, affiliation = 0, Zone = Zone((0, 0), (5, 5)))
        Building1.CharacterModels["Test Model"] = CharModel

        Char = Building1.createCharacter("Test Model")
        assert Char.life        == CharModel.life
        assert Char.strength    == CharModel.strength
        assert Char.Zone.x      == Building1.Zone.x
        assert Char.Zone.y      == Building1.Zone.y
        assert Char.Zone.width  == CharModel.Zone.width
        assert Char.Zone.height == CharModel.Zone.height
        assert Char.affiliation == CharModel.affiliation

    def test_building_create_character_failure(self):
        Building1 = Building(life = 10, affiliation = 0, Zone = Zone((0, 0), (1, 1)))
        CharModel = Character(strength = 10, life = 10, affiliation = 0, Zone = None)
        Building1.CharacterModels["Test Model"] = CharModel
        self.assertRaises(KeyError, Building1.createCharacter, "Invalid Test Model")
