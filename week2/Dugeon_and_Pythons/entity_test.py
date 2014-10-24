#entity_test.py

import unittest
from entity import Entity
from weapon import Weapon

class TestEntity(unittest.TestCase): 
    def setUp(self):
        self.new_Entity = Entity("Bron", 100)

    def test_Entity_name(self):
        self.assertEqual("Bron", self.new_Entity.name)

    def test_Entity_health(self):
        self.assertEqual(100,self.new_Entity.health)

    def test_get_health(self):
        new_Entity1 = Entity("Bron", 90)
        self.assertEqual(90,new_Entity1.get_health())

    def test_is_alive_true(self):
        self.assertTrue(self.new_Entity.is_alive())

    def test_is_alive_false(self):
        new_dead_Entity = Entity("Bron", 0)
        self.assertFalse(new_dead_Entity.is_alive())

    def test_take_damage(self):
        self.assertEqual(90,self.new_Entity.take_damage(10))

    def test_take_damage_zero(self):
        self.assertEqual(0, self.new_Entity.take_damage(110))

    def test_take_healing_false(self):
        new_healing_Entity = Entity("Bron", 0,)
        result = new_healing_Entity.take_healing(10)
        self.assertEqual(0,new_healing_Entity.health)
        self.assertFalse(result)

    def test_take_healing_true(self):
        new_healing_Entity = Entity("Bron", 100)
        new_healing_Entity.take_damage(30)
        result = new_healing_Entity.take_healing(30)
        self.assertEqual(100,new_healing_Entity.health)
        self.assertTrue(result)

    def test_take_healing_above_max_health(self):
        new_healing_Entity = Entity("Bron", 100)
        result = new_healing_Entity.take_healing(20)
        self.assertEqual(100, new_healing_Entity.health)
        self.assertTrue(result)

    def test_has_weapon(self):
        weapon = Weapon("Axe", 34, 0.5)
        self.new_Entity.equip_weapon(weapon)
        self.assertTrue(self.new_Entity.has_weapon())

    def test_equip_1_weapon(self):
        weapon = Weapon("Axe", 34, 0.5)
        self.new_Entity.equip_weapon(weapon)
        self.assertEqual("Axe", self.new_Entity.weapon.type)

    def test_equip_new_weapon_and_the_old_one_is_discarded(self):
        weapon1 = Weapon("Axe", 34, 0.5)
        weapon2 = Weapon("Sword", 34, 0.5)
        self.new_Entity.equip_weapon(weapon1)
        self.new_Entity.equip_weapon(weapon2)
        self.assertEqual("Sword", self.new_Entity.weapon.type)

    def test_attack_zero(self):
        self.assertEqual(0, self.new_Entity.attack())

    def test_attack_not_zero(self):
        weapon = Weapon("Axe", 34, 0.5)
        self.new_Entity.equip_weapon(weapon)
        self.assertEqual(34, self.new_Entity.attack())


if __name__ == '__main__':
    unittest.main()