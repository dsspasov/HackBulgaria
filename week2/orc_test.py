#orc_test.py
import unittest
from orc import Orc
from weapon import Weapon

class TestOrc(unittest.TestCase):

    def test_orc_barserk_larger(self):
        evil_orc = Orc('karakondjul', 100 , 2.5)
        self.assertEqual(2, evil_orc.barserk)
    def test_orc_barserk_smaller(self):
        evil_orc = Orc('karakondjul', 100 , 0.5)
        self.assertEqual(1, evil_orc.barserk)
    def test_orc_barserk_normall(self):
        evil_orc = Orc('karakondjul', 100 , 1.5)
        self.assertEqual(1.5, evil_orc.barserk)

    def test_barserk_attack(self):
        evil_orc = Orc('karakondjul', 100 , 1.5)
        weapon = Weapon("Axe",2,0.5)
        evil_orc.equip_weapon(weapon)
        self.assertEqual(3,evil_orc.attack())

if __name__ == '__main__':
    unittest.main()