#DungeonsAndPythons_test.py
import unittest
from hero import Hero

class TestHero(unittest.TestCase): 
    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")
#    def test_hero_name(self):
#        self.assertEqual("Bron", self.bron_hero.name)

#    def test_hero_health(self):
#        self.assertEqual(100,self.bron_hero.health)

    def test_hero_nickname(self):
        self.assertEqual("DragonSlayer", self.bron_hero.nickname)

    def test_know_as(self):
        self.assertEqual("Bron the DragonSlayer", self.bron_hero.know_as())

#    def test_get_health(self):
#        hero = Hero("Bron", 90, "DragonSlayer")
#        self.assertEqual(90,hero.get_health())

#    def test_is_alive_true(self):
#        self.assertTrue(self.bron_hero.is_alive())

#    def test_is_alive_false(self):
#        hero = Hero("Bron", 0, "DragonSlayer")
#        self.assertFalse(hero.is_alive())

#    def test_take_damage(self):
#        self.assertEqual(90,self.bron_hero.take_damage(10))

#    def test_take_damage_zero(self):
#        self.assertEqual(0, self.bron_hero.take_damage(110))

 #   def test_take_healing_false(self):
 #       hero = Hero("Bron", 0, "DragonSlayer")
#        result = hero.take_healing(10)
#        self.assertEqual(0,hero.health)
#        self.assertFalse(result)

#    def test_take_healing_true(self):
#        hero = Hero("Bron", 100, "DragonSlayer")
#        hero.take_damage(30)
#        result = hero.take_healing(30)
#        self.assertEqual(100,hero.health)
#        self.assertTrue(result)

#    def test_take_healing_above_max_health(self):
#        hero = Hero("Bron", 100, "DragonSlayer")
#        result = hero.take_healing(20)
#        self.assertEqual(100, hero.health)
#        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()