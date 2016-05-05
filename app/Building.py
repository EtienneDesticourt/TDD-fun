from app.Character import Character

class Building(object):
    def __init__(self, position=(0,0)):
        self.CharacterModels = {}
        self.position = position

    def createCharacter(self, modelName):
        Model = self.CharacterModels[modelName]
        Char = Character(position = self.position, strength = Model.strength)
        return Char
