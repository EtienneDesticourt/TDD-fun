import unittest
from app.Character import Character
from app.Entity import Entity
from pygame import Rect as Zone

class CharacterTestCase(unittest.TestCase):

    def test_character_move(self):
        Char = Character(strength = 10, life = 10, affiliation = 0, Zone = Zone((0, 1), (1, 1)))
        Char.speed = (2, 3)
        Char.move()
        assert Char.Zone.x == 2
        assert Char.Zone.y == 4

    def test_character_attack(self):
        Char = Character(strength = 5, life = 10, affiliation = 0, Zone = None)
        Ent = Entity(life = 10, affiliation = 1, Zone = None)
        Char.attack(Ent)
        assert Ent.life == 5

    def test_character_build(self):
        Char =  Character(strength = 5, life = 10, affiliation = 0, Zone = None)
        Ent = Entity(life = 0, affiliation = 1, Zone = None)
        Char.build(Ent)
        assert Ent.life == 5
