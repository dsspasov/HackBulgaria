#orc.py
from entity import Entity 
class Orc(Entity):
    def __init__(self, name, health, barserk):
        super().__init__(name,health)
        self._set_barserk(barserk)

    def _set_barserk(self, barserk):
        
        if barserk>2.0:self.barserk = 2.0
        elif barserk<1.0:self.barserk = 1.0
        else:self.barserk = barserk

    def attack(self):
        return self.weapon.damage*self.barserk if self.has_weapon() else 0

