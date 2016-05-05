import unittest
from app.Character import Character
from app.Entity import Entity

class CharacterTestCase(unittest.TestCase):

    def test_character_move(self):
        Char = Character()
        Char.position = (0, 1)
        Char.speed = (2, 3)
        Char.move()
        assert Char.position == (2, 4)

    def test_character_attack(self):
        Char = Character()
        Ent = Entity()
        Ent.life = 10
        Char.strength = 5
        Char.attack(Ent)
        assert Ent.life == 5

    def test_character_build(self):
        Char =  Character()
        Ent = Entity()
        Ent.life = 0
        Char.strength = 5
        Char.build(Ent)
        assert Ent.life == 5
