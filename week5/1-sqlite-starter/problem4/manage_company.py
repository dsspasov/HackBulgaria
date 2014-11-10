import sqlite3


class manage_company:

    def __init__(self):
        self.connection = sqlite3.connect('mydb')
        # self.cursor = self.connection.cursor()

    def list_employees(self):
        self.connection.row_factory = sqlite3.Row
        cursor = self.connection.cursor()
        result = cursor.execute("SELECT id,name, position FROM users")
        # result_fetched = result.fetchall()
        for row in result:
            print("{} - {} - {}".format(row['id'], row['name'], row['position']))
        self.connection.commit()

    def monthly_spending(self):
        self.connection.row_factory = sqlite3.Row
        cursor = self.connection.cursor()
        result = cursor.execute(
            "SELECT SUM(\"monthly_salary\") AS total_spend_for_month FROM users")
        total_expenditure = result.fetchone()
        self.connection.commit()
        return total_expenditure['total_spend_for_month']
        # print(total_expenditure['total_spend_for_month'])

    def yearly_spending(self):
        self.connection.row_factory = sqlite3.Row
        cursor = self.connection.cursor()
        result = cursor.execute("SELECT SUM(\"yearly_bonus\") AS total_spend_for_year FROM users")
        total_year_bonus = result.fetchone()
        self.connection.commit()
        return (self.monthly_spending() + total_year_bonus['total_spend_for_year'])
        # print(r['total_spend_for_year'])

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position)
                          VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
        self.connection.commit()

    def delete_employee(self, id):
        cursor = self.connection.cursor()
        string = " DELETE FROM users Where id ={}".format(id)
        cursor.execute(string)
        self.connection.commit()

    def update_employee(self, id, name, monthly_salary, yearly_bonus, position):
        cursor = self.connection.cursor()

        cursor.execute('''UPDATE users SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ? ''',
                       (name, monthly_salary, yearly_bonus, position, id))
        self.connection.commit()
        # cursor.execute(string)

    def option(self):
        print("enter help")

        while(True):
            command = input("Command>")
            command = command.split(" ")
            if command[0] == "help":
                print('''    help
    finish
    list_employees
    monthly_spending
    yearly_spending
    add_employee
    delete_employee <id>
    update_emplyee <id>''')
            if command[0] == "finish":
                print("FINISH")
                break
            if command[0] == "list_employees":
                self.list_employees()
            if command[0] == "monthly_spending":
                print(self.monthly_spending())
            if command[0] == "yearly_spending":
                print(self.yearly_spending())
            if command[0] == "add_employee":
                name = input("Name>")
                monthly_salary = (int)(input("monthly_salary>"))
                yearly_bonus = (int)(input("yearly_bonus>"))
                position = input("Postion>")
                self.add_employee(name, monthly_salary, yearly_bonus, position)
            if command[0] == "delete_employee":
                id = command[1]
                self.delete_employee(id)
            if command[0] == "update_employee":
                id = command[1]
                name = input("Name>")
                monthly_salary = (int)(input("monthly_salary>"))
                yearly_bonus = (int)(input("yearly_bonus>"))
                position = input("Postion>")
                self.update_employee(id, name, monthly_salary, yearly_bonus, position)
        self.connection.close()


def main():
    a = manage_company()
    a.option()
    #a.add_employee("a", 100, 100, "b")
    #a.update_employee(6, 'c', 200, 300, 'd')
    # a.delete_employee(6)
    # a.list_employees()
    # a.monthly_spending()
    # a.yearly_spending()


if __name__ == '__main__':
    main()
