
#conn.row_factory = sqlite3.Row
# for row in result:
#    row['id'].....

import sqlite3


class data_base:

    def __init__(self):
        self.name = 'mydb'
        self.db = sqlite3.connect(self.name)
        self.cursor = self.db.cursor()

    def create_db(self):
        self.cursor.execute('''
            CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                               monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
        ''')
        self.db.commit()

        self.insert_in_db("Ivan Ivanov", 5000, 10000, "Software Developer")
        self.insert_in_db("Rado Rado", 500, 0, "Technical Support Intern")
        self.insert_in_db("Ivo Ivo", 10000, 100000, "CEO")
        self.insert_in_db("Petar Petrov", 3000, 1000, "Marketing Manager")
        self.insert_in_db("Maria Georgieva", 8000, 10000, "COO")

        self.db.commit()
        self.db.close()

    def insert_in_db(self, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position)
                          VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))

        self.db.commit()

#    def select(self):
# conn = sqlite3.connect(self.name)
# cursor = conn.cursor()
#
#        result = self.cursor.execute("SELECT * FROM users")
#
#        for row in result:
#            print(row)
#        self.db.close()


def main():
    a = data_base()
    a.create_db()
    #a.insert_in_db("Ivan Ivanov", 5000, 10000, "Software Developer")
    #a.insert_in_db("Rado Rado", 500, 0, "Technical Support Intern")
    #a.insert_in_db("Ivo Ivo", 10000, 100000, "CEO")
    #a.insert_in_db("Petar Petrov", 3000, 1000, "Marketing Manager")
    #a.insert_in_db("Maria Georgieva", 8000, 10000, "COO")
    # a.select()

if __name__ == '__main__':
    main()
