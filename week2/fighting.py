#fighting.py
import random

from hero import Hero 
from orc import Orc
from weapon import Weapon 

class Fighting:
    def __init__(self,hero,orc):
        self.hero = hero
        self.orc = orc
    def flip_coin(self):
        chance = random.randint(1,100)
        if(chance<=50):return self.hero
        else:return self.orc

    def simulate_fight(self):
        if isinstance(self.flip_coin(), Hero):
            first_attacker = self.hero
            second_attacker= self.orc
        else:
            first_attacker = self.orc
            second_attacker= self.hero

        if not first_attacker.has_weapon():
            first_attacker.equip_weapon(Weapon("stick",1 ,0.01))
        if not second_attacker.has_weapon():
            second_attacker.equip_weapon(Weapon("stick", 1 ,0.01))

        print ("{} attacks first".format(first_attacker.name))
        while True:

            damage = first_attacker.attack()
            print ("{} attacks with {} damage".format(first_attacker.name, damage))

            second_attacker.take_damage(damage)
            print ("{} takes damage {}".format(second_attacker.name,damage))

            if not second_attacker.is_alive():
                print ("{} is dead".format(second_attacker.name))
                print('\n')
                return first_attacker

            damage = second_attacker.attack()
            print ("{} attacks with {} damage".format(second_attacker.name, damage))

            first_attacker.take_damage(damage)
            print ("{} takes damage {}".format(first_attacker.name,damage))

            if not first_attacker.is_alive():
                print ("{} is dead".format(first_attacker.name))
                print('\n')
                return second_attacker