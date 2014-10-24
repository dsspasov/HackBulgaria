#entity.py_
class Entity:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health

    def get_health(self):
        return self.health

    def is_alive(self):
        return (True if self.health>0 else False)

    def take_damage(self,damage_points):

        self.health -= damage_points
        if not self.is_alive():
            self.health = 0
        return self.health

    def take_healing(self, healing_points):
        
        if self.health == 0:
            return False
        else:
            if self.health+healing_points > self._MAX_HEALTH:
                self.health = self._MAX_HEALTH
            else:
                self.health += healing_points
            return True

    def has_weapon(self):
        return hasattr(self,"weapon")
        
    def equip_weapon(self,weapon):
        setattr(self,"weapon",weapon)

    def attack(self):
        return self.weapon.damage if self.has_weapon() else 0
