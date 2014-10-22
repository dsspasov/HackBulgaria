#dungeon_test.py

import unittest
import os

from dungeon import Dungeon

from fighting import Fighting
from hero import Hero 
from orc import Orc
from weapon import Weapon 

class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.content = 'S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S'
        self.filename = "basic_dungeon.txt" 
        self.file = open(self.filename,'w')
        self.file.write(self.content)
        self.file.close()

        ##-------------------------

        self.new_map = Dungeon(self.filename)
    def tearDown(self):
        #pass
        os.remove(self.filename)

    

    def test_spawn_true(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        player2 = Orc('karakondjul', 100 , 1.5)
        self.assertTrue(self.new_map.spawn(player1.name, player1))
        self.assertTrue(self.new_map.spawn(player2.name, player2))

        #self.new_map.print_map()

    def test_spawn_false(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        player2 = Orc('karakondjul', 100 , 1.5)
        player3 = Hero("Bron1", 100, "DragonSlayer")
        self.assertTrue(self.new_map.spawn(player1.name, player1))
        self.assertTrue(self.new_map.spawn(player2.name, player2))
        self.assertFalse(self.new_map.spawn(player3.name, player3))

        #self.new_map.print_map()

    def test_print_map(self):
        
        self.assertEqual(self.new_map.get_content(),self.content)
        #print(self.content)
        #self.new_map.print_map()

    def test_move_right_true(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        self.new_map.spawn(player1.name, player1)
        self.assertTrue(self.new_map.move(player1.name,"right"))

    def test_move_right_false(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        self.new_map.spawn(player1.name, player1)
        self.new_map.move(player1.name,"right")
        self.assertFalse(self.new_map.move(player1.name,"right"))

    def test_move_left_true(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        self.new_map.spawn(player1.name, player1)
        self.new_map.move(player1.name,"right")

        self.assertTrue(self.new_map.move(player1.name,"left"))

    def test_move_left_false(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        self.new_map.spawn(player1.name, player1)
        self.assertFalse(self.new_map.move(player1.name,"left"))

    def test_move_up_true(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        player2 = Orc('karakondjul', 100 , 1.5)
        self.new_map.spawn(player1.name, player1)
        self.new_map.spawn(player2.name, player2)
        self.assertTrue(self.new_map.move(player2.name,"up"))

    def test_move_up_false(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        self.new_map.spawn(player1.name, player1)
        self.assertFalse(self.new_map.move(player1.name,"up"))

    def test_move_down_true(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        self.new_map.spawn(player1.name, player1)

        self.new_map.move(player1.name,"right")
        self.assertTrue(self.new_map.move(player1.name,"down"))

    def test_move_down_false(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        player2 = Orc('karakondjul', 100 , 1.5)
        self.new_map.spawn(player1.name, player1)
        self.new_map.spawn(player2.name, player2)
        self.assertFalse(self.new_map.move(player2.name,"down"))

    def test_move_right_and_fight(self):
        player1 = Hero("Bron", 10, "DragonSlayer")
        player2 = Orc('karakondjul', 100 , 1.5)
        self.new_map.spawn(player1.name, player1)
        self.new_map.spawn(player2.name, player2)
        self.new_map.move(player1.name, 'right')
        #self.new_map.print_map()

    def test_move_left_and_fight(self):
        player1 = Hero("Bron", 10, "DragonSlayer")
        player2 = Orc('karakondjul', 10 , 1.5)
        self.new_map.spawn(player1.name, player1)
        self.new_map.spawn(player2.name, player2)
        self.new_map.move(player2.name, 'left')
        #self.new_map.print_map()

    def test_move_up_and_fight(self):
        player1 = Hero("Bron", 10, "DragonSlayer")
        player2 = Orc('karakondjul', 100 , 1.5)
        self.new_map.spawn(player1.name, player1)
        self.new_map.spawn(player2.name, player2)
        self.new_map.move(player1.name, 'right')
        #self.new_map.print_map()
        self.new_map.move(player2.name, 'up')

        #self.new_map.print_map()

    def test_move_down_and_fight(self):
        player1 = Hero("Bron", 100, "DragonSlayer")
        player2 = Orc('karakondjul', 10 , 1.5)
        self.new_map.spawn(player1.name, player1)
        self.new_map.spawn(player2.name, player2)
        self.new_map.move(player1.name, 'right')
        #self.new_map.print_map()
        self.new_map.move(player1.name, 'down')

        #self.new_map.print_map()




if __name__ == '__main__':
    unittest.main()