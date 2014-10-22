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
        #    return True
        #return False

    def take_damage(self,damage_points):

        self.health -= damage_points
        if not self.is_alive():
            self.health = 0
        return self.health

        #if(self.health - damage_points<0):
        #    self.health =0
        #else:
        #    self.health -= damage_points
        #return self.health

    def take_healing(self, healing_points):
        
        if self.health == 0:
            return False
        else:
            if self.health+healing_points > self._MAX_HEALTH:
                self.health = self._MAX_HEALTH
            else:
                self.health += healing_points
            return True




#            self.health += healing_points
#            if self.health>self._MAX_HEALTH:
#                self.health = self._MAX_HEALTH
#                return True
#            return True


    def has_weapon(self):
        return hasattr(self,"weapon")
        
    def equip_weapon(self,weapon):
        setattr(self,"weapon",weapon)

    def attack(self):
        return self.weapon.damage if self.has_weapon() else 0
        #if not self.has_weapon():
        #    return 0
        #else:
        #    return self.weapon.damage

