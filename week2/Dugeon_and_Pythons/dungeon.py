#dungeon.py

from fighting import Fighting
from hero import Hero 
from orc import Orc
from weapon import Weapon 

class Dungeon:

    def __init__(self, filename):
        self.filename = filename
        self._name_hero = ''
        self._name_orc = ''
        self._hero = Hero('',0,'')
        self._orc = Orc('',0,0)

    def get_content(self):
        file = open(self.filename,"r")
        content = file.read()
        file.close()
        return content

    def put_content(self,content):
        file = open(self.filename,'w')
        file.write(content)
        file.close()

    def print_map(self):

        print(self.get_content())

    def spawn(self,name,player_type):
        dungeon_map = self.get_content()
        if 'S' in dungeon_map:
            if isinstance(player_type, Hero):
                dungeon_map = dungeon_map.replace('S','H', 1)
                self._name_hero = name
                self._hero = player_type
                self.put_content(dungeon_map)
            else:
                dungeon_map = dungeon_map.replace('S','O', 1)
                self._name_orc = name
                self._orc = player_type
                self.put_content(dungeon_map)
            return True

        return False

    def map_to_list(self):
        content = self.get_content()
        content = content.split('\n')
        result = []
        for index in range(len(content)):
            result.append([])
            n = len(list(content[index]))
            result[index]=list(content[index])
            result[index].append(' ')
            result[index].insert(0,' ')
        n+=2
        result.insert(0,[' ']*n)
        result.append([' ']*n)
        #print(result)
        return result

    def list_to_map(self,l):
        l.pop()
        l.pop(0)
        content = ''
        for each in l:
            content=content+''.join(each)+'\n'
        return content

    def get_index(self,element):
        m = self.map_to_list()
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == element:
                    return (i,j)


#---------------NEW-------------------------------
    
    def next_position(self, way,current_x,current_y):
        if way == "right":
            next_pos_x = current_x
            next_pos_y = current_y+1

        if way == "left":
            next_pos_x = current_x
            next_pos_y = current_y-1

        if way == "up":
            next_pos_x = current_x-1
            next_pos_y = current_y

        if way == "down":
            next_pos_x = current_x+1
            next_pos_y = current_y
        return (next_pos_x,next_pos_y)

    def put_updated_map_to_file(self, new_map):
        s = self.list_to_map(new_map)
        self.put_content(s)

    def initialization(self,player_name):
        if player_name == self._name_hero:
            player_index = self.get_index('H')
            player_moving = 'H'
            player_type_moving = Hero
            player_not_moving = 'O'
        else:
            player_index = self.get_index('O')
            player_moving = 'O'
            player_type_moving = Orc
            player_not_moving = 'H'

        return (player_index, player_moving, player_type_moving, player_not_moving)

    def fing_opponent(self,current_x, current_y, next_pos_x, next_pos_y, Lmap, player_moving, player_not_moving, player_type_moving):

        if Lmap[next_pos_x][next_pos_y] == player_not_moving:#O
            fight = Fighting(self._hero,self._orc)
            winner = fight.simulate_fight()
            if isinstance(winner,player_type_moving):
                Lmap[next_pos_x][next_pos_y] = player_moving#H
                Lmap[current_x][current_y] = '.'
                self.put_updated_map_to_file(Lmap)
                return True
            else:
                Lmap[current_x][current_y] = '.'
                self.put_updated_map_to_file(Lmap)
                return False

    def move(self, name, direction):

        list_map = self.map_to_list()

        index = self.initialization(name)[0]
        moving = self.initialization(name)[1]
        type_moving = self.initialization(name)[2]
        not_moving = self.initialization(name)[3]

        x = index[0]
        y = index[1]
            
        rows = len(list_map)
        cols = len(list_map[x])

        next_x = self.next_position(direction, x, y)[0]
        next_y = self.next_position(direction, x, y)[1]

        if next_x<0 or next_x>rows or next_y<0 or next_y>cols or list_map[next_x][next_y] == '#':
                return False

        if list_map[next_x][next_y] == '.':
            list_map[next_x][next_y] = moving
            list_map[x][y] = '.'
            self.put_updated_map_to_file(list_map)
            return True

        if self.fing_opponent(x, y, next_x, next_y, list_map, moving, not_moving, type_moving):
            return True
        else:
            return False
#---------------------------------------------------------------------------------------------------------------------
