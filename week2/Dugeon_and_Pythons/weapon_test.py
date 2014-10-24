#weapon_test.py
import unittest
import random
from weapon import Weapon 
class TestWeapon(unittest.TestCase):
    def test_type(self):
        new_weapon = Weapon("Mighty Axe", 25, 0.2)
        self.assertEqual("Mighty Axe", new_weapon.type)

    def test_damage(self):
        new_weapon = Weapon("Mighty Axe", 25, 0.2)
        self.assertEqual(25, new_weapon.damage)

    def test_critical_strike_percent(self):
        new_weapon = Weapon("Mighty Axe", 25, 0.2)
        self.assertEqual(0.2, new_weapon.critical_strike_percent)

    def test_critical_hit_true_and_false(self):
        new_weapon = Weapon("Mighty Axe", 25, 0.2)
        results = []
        for i in range(10):
            results.append(new_weapon.critical_hit())
        self.assertIn(True, results)
        self.assertIn(False, results)

if __name__ == '__main__':
    unittest.main()