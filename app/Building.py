from app.Character import Character
from app.Entity import Entity
from pygame import Rect as Zone

class Building(Entity):
    def __init__(self, life, affiliation, Zone):
        super().__init__(life, affiliation, Zone)
        self.CharacterModels = {}

    def createCharacter(self, modelName):
        Model = self.CharacterModels[modelName]
        CharZone = Zone((self.Zone.x, self.Zone.y), (Model.Zone.width, Model.Zone.height))
        Char = Character(strength = Model.strength, life = Model.life, affiliation = Model.affiliation, Zone = CharZone)
        return Char
