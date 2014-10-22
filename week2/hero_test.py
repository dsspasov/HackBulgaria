#DungeonsAndPythons_test.py
import unittest
from hero import Hero

class TestHero(unittest.TestCase): 
    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")

    def test_hero_nickname(self):
        self.assertEqual("DragonSlayer", self.bron_hero.nickname)

    def test_know_as(self):
        self.assertEqual("Bron the DragonSlayer", self.bron_hero.know_as())

if __name__ == '__main__':
    unittest.main()