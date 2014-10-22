#weapon.py
import random
class Weapon:
    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self._set_critical_strike_percent(critical_strike_percent)
        self._CRITICAL_DAMAGE = damage

    def _set_critical_strike_percent(self,critical_strike_percent):
        if critical_strike_percent>=0 and critical_strike_percent<=1.0:
            self.critical_strike_percent = critical_strike_percent
        else:
            raise ValueError

    def critical_hit(self):
        current_percet = random.uniform(0.0, 1.0) 
        if current_percet<=self.critical_strike_percent:
            self._CRITICAL_DAMAGE = 2*self.damage
            return True
        else:
            self._CRITICAL_DAMAGE = self.damage
            return False

