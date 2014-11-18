import sqlite3


class CreateDatabase:

    def __init__(self):
        self.name = 'mydb'
        self.db = sqlite3.connect(self.name)
        self.db.execute('pragma foreign_keys=ON')
        self.cursor = self.db.cursor()

    def create_movies_table(self):
        self.cursor.execute(
            '''CREATE TABLE movies(id INTEGER PRIMARY KEY, name TEXT, rating REAL)'''
        )
        self.db.commit()

    def create_projection_table(self):
        self.cursor.execute(
            '''CREATE TABLE projections(id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                type TEXT, date TEXT, time TEXT, seats INTEGER, FOREIGN KEY(movie_id) REFERENCES movies(id))''')
        self.db.commit()

    def create_reservations_table(self):
        self.cursor.execute(
            '''CREATE TABLE reservations(id INTEGER PRIMARY KEY,
            username TEXT, projection_id INTEGER,
            row INTEGER, col INTEGER,
            FOREIGN KEY(projection_id) REFERENCES projections(id))''')
        self.db.commit()

    def insert_info(self):
        movies_info = [('The Hunger Games: Catching Fire', 7.9),
                       ('Wreck-It Ralph', 7.8),
                       ('Her', 8.3)
                       ]

        projections_info = [(1, '3D', '2014-04-01', '19:10', 100),
                            (1, '2D', '2014-04-01', '19:00', 100),
                            (1, '4DX', '2014-04-02', '21:00', 100),
                            (3, '2D', '2014-04-05', '20:20', 100),
                            (2, '3D', '2014-04-02', '22:00', 100),
                            (2, '2D', '2014-04-02', '19:30', 100)]

        reservations_info = [('RadoRado', 1, 2, 1),
                             ('RadoRado', 1, 3, 5),
                             ('RadoRado', 1, 7, 8),
                             ('Ivo', 3, 1, 1),
                             ('Ivo', 3, 1, 2),
                             ('Mysterious', 5, 2, 3),
                             ('Mysterious', 5, 2, 4)]
        self.cursor.executemany("INSERT INTO movies(name,rating) VALUES(?,?)", movies_info)
        self.cursor.executemany(
            "INSERT INTO projections(movie_id, type, date, time, seats) VALUES(?,?,?,?,?)", projections_info)
        self.cursor.executemany(
            '''INSERT INTO reservations(username, projection_id, row, col)
                VALUES(?,?,?,?)''', reservations_info)
        self.db.commit()


def main():
    a = CreateDatabase()
    a.create_movies_table()
    a.create_projection_table()
    a.create_reservations_table()
    a.insert_info()

if __name__ == '__main__':
    main()
