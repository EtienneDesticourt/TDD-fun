

class Character(object):
    def __init__(self, position=(0, 0), speed=(0,0), strength=0):
        self.position = position
        self.speed = speed
        self.strength = strength

    def move(self):
        x, y = self.position
        dx, dy = self.speed
        self.position = (x + dx, y + dy)

    def attack(self, Entity):
        Entity.life -= self.strength

    def build(self, Entity):
        Entity.life += self.strength
