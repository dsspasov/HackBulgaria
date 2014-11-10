
#conn.row_factory = sqlite3.Row
# for row in result:
#    row['id'].....

import sqlite3


class data_base:

    def __init__(self):
        self.name = 'mydb'

    def create_db(self):
        db = sqlite3.connect(self.name)
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                               monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
        ''')
        db.commit()
        db.close()

    def insert_in_db(self, name, monthly_salary, yearly_bonus, position):
        db = sqlite3.connect(self.name)
        cursor = db.cursor()
        #name = "Ivan Ivanov"
        #monthly_salary = 5000
        #yearly_bonus = 10000
        #position = "Software Developer"

        cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position)
                          VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
        db.commit()
        db.close()

    def select(self):
        conn = sqlite3.connect(self.name)
        cursor = conn.cursor()

        result = cursor.execute("SELECT * FROM users")

        for row in result:
            print(row)
        conn.close()


def main():
    a = data_base()
    a.create_db()
    a.insert_in_db("Ivan Ivanov", 5000, 10000, "Software Developer")
    a.insert_in_db("Rado Rado", 500, 0, "Technical Support Intern")
    a.insert_in_db("Ivo Ivo", 10000, 100000, "CEO")
    a.insert_in_db("Petar Petrov", 3000, 1000, "Marketing Manager")
    a.insert_in_db("Maria Georgieva", 8000, 10000, "COO")
    a.select()

if __name__ == '__main__':
    main()
