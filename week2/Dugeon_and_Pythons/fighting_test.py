#fighting_test.py
import unittest
from fighting import Fighting
from hero import Hero 
from orc import Orc
from weapon import Weapon 

class TestFighting(unittest.TestCase):
    def test_which_player_starts(self):
        hero = Hero("Bron", 100, "DragonSlayer")
        evil_orc = Orc('karakondjul', 100 , 1.5)
        fight = Fighting(hero,evil_orc)
        result = fight.flip_coin()
        self.assertTrue(isinstance(result,Hero) or isinstance(result,Orc))
    def test_fight(self):
        hero = Hero("Bron", 1000, "DragonSlayer")
        evil_orc = Orc('karakondjul', 100 , 1.5)
        weapon1 = Weapon("Axe", 34, 0.5)
        weapon2 = Weapon("Sword", 34, 0.5)
        hero.equip_weapon(weapon1)
        evil_orc.equip_weapon(weapon2)
        fight = Fighting(hero,evil_orc)
        winner = fight.simulate_fight()
        self.assertTrue(isinstance(winner,Hero) or isinstance(winner,Orc))

    def test_hero_wins(self):
        hero = Hero("Bron", 100, "DragonSlayer")
        evil_orc = Orc('karakondjul', 50 , 1.5)
        weapon1 = Weapon("Axe", 34, 0.5)
        weapon2 = Weapon("Sword", 1, 0.5)
        hero.equip_weapon(weapon1)
        evil_orc.equip_weapon(weapon2)
        fight = Fighting(hero,evil_orc)
        winner = fight.simulate_fight()
        self.assertTrue(isinstance(winner,Hero))

    def test_orc_wins(self):
        hero = Hero("Bron", 50, "DragonSlayer")
        evil_orc = Orc('karakondjul', 100 , 1.5)
        weapon1 = Weapon("Axe", 1, 0.5)
        weapon2 = Weapon("Sword", 34, 0.5)
        hero.equip_weapon(weapon1)
        evil_orc.equip_weapon(weapon2)
        fight = Fighting(hero,evil_orc)
        winner = fight.simulate_fight()
        self.assertTrue(isinstance(winner,Orc))

    def test_fight_with_no_weapons(self):
        hero = Hero("Bron", 15, "DragonSlayer")
        evil_orc = Orc('karakondjul', 10 , 1.5)
        #weapon1 = Weapon("Axe", 5, 0.5)
        #weapon2 = Weapon("Sword", 34, 0.5)
        #hero.equip_weapon(weapon1)
        #evil_orc.equip_weapon(weapon2)
        fight = Fighting(hero,evil_orc)
        winner = fight.simulate_fight()
        self.assertTrue(isinstance(winner,Hero) or isinstance(winner,Orc))
    
    def test_fight_with_one_weapon(self):
        hero = Hero("Bron", 15, "DragonSlayer")
        evil_orc = Orc('karakondjul', 10 , 1.5)
        weapon1 = Weapon("Axe", 5, 0.5)
        hero.equip_weapon(weapon1)
        fight = Fighting(hero,evil_orc)
        winner = fight.simulate_fight()
        self.assertTrue(isinstance(winner,Hero) or isinstance(winner,Orc))

if __name__ == '__main__':
    unittest.main()