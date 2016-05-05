from app.Entity import Entity

class Character(Entity):
    def __init__(self, strength, life, affiliation, Zone):
        super().__init__(life, affiliation, Zone)
        self.strength = strength
        self.speed = (0, 0)

    def move(self):
        self.Zone.move_ip(self.speed)

    def attack(self, Entity):
        Entity.life -= self.strength

    def build(self, Entity):
        Entity.life += self.strength
