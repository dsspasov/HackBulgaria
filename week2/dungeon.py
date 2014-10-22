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
#------------------------------------
    def get_content(self):
        file = open(self.filename,"r")
        content = file.read()
        file.close()

        return content
    def put_content(self,content):
        file = open(self.filename,'w')
        file.write(content)

        file.close()
#------------------------------------
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
        for index in range(len(content)):
            content[index]=list(content[index])
        return content

    def list_to_map(self,l):
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

    def move(self, name, direction):

        list_map = self.map_to_list()
        if name == self._name_hero:
            index = self.get_index('H')
            x = index[0]
            y = index[1]
            moving = self._hero
            not_moving = self._orc
        else:
            index = self.get_index('O')
            x = index[0]
            y = index[1]
            moving = self._orc
            not_moving = self._hero

#-------------------OLD---------------------------
        if direction == "right":
            next_x = x
            next_y = y+1
            if list_map[x][y+1] == '#' or y+1>len(list_map[x]):
                return False

            if name == self._name_hero:
                #index = self.get_index('H')
                #x = index[0]
                #y = index[1]
                if list_map[x][y+1] == '.' and y+1<=len(list_map[x]):

                    list_map[x][y+1] = 'H'
                    list_map[x][y] = '.'
                    s = self.list_to_map(list_map)
                    self.put_content(s)

                    return True
                else:
                    if list_map[x][y+1] == 'O':
                        fight = Fighting(self._hero,self._orc)
                        winner = fight.simulate_fight()
                        if isinstance(winner,Hero):
                            list_map[x][y+1] = 'H'
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)
                        else:
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)

#                    if list_map[x][y+1] == '#' or y+1>len(list_map[x]):
#                        return False

            else:
                #index = self.get_index('O')
                #x = index[0]
                #y = index[1]
                if list_map[x][y+1] == '.' and y+1<=len(list_map[x]):

                    list_map[x][y+1] = 'O'
                    list_map[x][y] = '.'
                    s = self.list_to_map(list_map)
                    self.put_content(s)
                    
                    return True
                else:
                    if list_map[x][y+1] == 'H':
                        fight = Fighting(self._hero,self._orc)
                        winner = Fighting.simulate_fight()
                        if isinstance(winner,Hero):
                            list_map[x][y+1] = 'H'
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)
                        else:
                            list_map[x][y] = '.'
                            list_map[x][y+1] = 'O'
                            s = self.list_to_map(list_map)
                            self.put_content(s)

#                    if list_map[x][y+1] == '#' or y+1>len(list_map[x]):
#                        return False
        if direction == "left":
            if name == self._name_hero:
                index = self.get_index('H')
                x = index[0]
                y = index[1]

                if list_map[x][y-1] == '.' and y-1>=0:

                    list_map[x][y-1] = 'H'
                    list_map[x][y] = '.'
                    s = self.list_to_map(list_map)
                    self.put_content(s)

                    return True
                else:
                    if list_map[x][y-1] == 'O':
                        fight = Fighting(self._hero,self._orc)
                        winner = fight.simulate_fight()
                        if isinstance(winner,Hero):
                            list_map[x][y-1] = 'H'
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)
                        else:
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)

                    if list_map[x][y-1] == '#' or y-1<0:
                        return False
            else:
                index = self.get_index('O')
                x = index[0]
                y = index[1]
                if list_map[x][y-1] == '.' and y-1>=0:

                    list_map[x][y-1] = 'O'
                    list_map[x][y] = '.'
                    s = self.list_to_map(list_map)
                    self.put_content(s)
                    return True
                else:

                    if list_map[x][y-1] == 'H':
                        fight = Fighting(self._hero,self._orc)
                        winner = fight.simulate_fight()
                        if isinstance(winner,Hero):
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)
                        else:
                            list_map[x][y-1] = 'O'
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)

                    if list_map[x][y-1] == '#' or y-1<0:
                        return False
        if direction == "up":
            if name == self._name_hero:
                index = self.get_index('H')
                x = index[0]
                y = index[1]

                if list_map[x-1][y] == '.' and x-1>=0:

                    list_map[x-1][y] = 'H'
                    list_map[x][y] = '.'
                    s = self.list_to_map(list_map)
                    self.put_content(s)
                    return True
                else:

                    if list_map[x-1][y] == 'O':
                        fight = Fighting(self._hero,self._orc)
                        winner = fight.simulate_fight()
                        if isinstance(winner,Hero):
                            list_map[x-1][y] = 'H'
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)
                        else:
                            list_map[x][y] = '.'

                            s = self.list_to_map(list_map)
                            self.put_content(s)

                    if list_map[x-1][y] == '#' or x-1<0:
                        return False
            else:
                index = self.get_index('O')
                x = index[0]
                y = index[1]
                if list_map[x-1][y] == '.' and x-1>=0:

                    list_map[x-1][y] = 'O'
                    list_map[x][y] = '.'
                    s = self.list_to_map(list_map)
                    self.put_content(s)
                    return True
                else:

                    if list_map[x-1][y] == 'H':
                        fight = Fighting(self._hero,self._orc)
                        winner = fight.simulate_fight()
                        if isinstance(winner,Hero):
                            list_map[x-1][y] = 'H'
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)
                        else:
                            list_map[x-1][y] = 'O'
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)

                    if list_map[x-1][y] == '#' or x-1<0:
                        return False
        if direction == "down":
            if name == self._name_hero:
                index = self.get_index('H')
                x = index[0]
                y = index[1]

                if list_map[x+1][y] == '.' and x+1<=len(list_map):

                    list_map[x+1][y] = 'H'
                    list_map[x][y] = '.'
                    s = self.list_to_map(list_map)
                    self.put_content(s)
                    return True
                else:

                    if list_map[x+1][y] == 'O':
                        fight = Fighting(self._hero,self._orc)
                        winner = fight.simulate_fight()
                        if isinstance(winner,Hero):
                            list_map[x+1][y] = 'H'
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)
                        else:
                            list_map[x][y] = '.'
                            s = self.list_to_map(list_map)
                            self.put_content(s)

                    if list_map[x+1][y] == '#' or x+1>len(list_map):
                        return False
            else:
                index = self.get_index('O')
                x = index[0]
                y = index[1]
                if x+1==len(list_map):
                    x=x-1
                    return False
                else:
                    if list_map[x+1][y] == '.' and x+1<=len(list_map):

                        list_map[x+1][y] = 'O'
                        list_map[x][y] = '.'
                        s = self.list_to_map(list_map)
                        self.put_content(s)
                        return True

                    else:
                        if list_map[x+1][y] == 'H':
                            fight = Fighting(self._hero,self._orc)
                            winner = fight.simulate_fight()
                            if isinstance(winner,Hero):
                                list_map[x][y] = '.'
                                s = self.list_to_map(list_map)
                                self.put_content(s)
                            else:
                                list_map[x][y] = '.'
                                list_map[x+1][y] = 'O'
                                s = self.list_to_map(list_map)
                                self.put_content(s)
                        if list_map[x+1][y] == '#':
                            return False        