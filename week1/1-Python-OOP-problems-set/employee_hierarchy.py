#employee_hierarchy.py
class Employee:
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name

class HourlyEmployee(Employee):
    def __init__(self,name,hourly_wage):
        self.hourly_wage = hourly_wage
        super(HourlyEmployee,self).__init__(name)
    def weeklyPay(self, hours):
        pay = 0
        if hours<=0:
            pay = 0
        elif hours>0 and hours < 40:
            pay = hours * self.hourly_wage
        else:
            pay = 40 * self.hourly_wage + (hours-40) * self.hourly_wage * 1.5
        return pay
class SalariedEmployee(Employee):
    def __init__(self,name,salary):
        self.salary = salary
        super(SalariedEmployee,self).__init__(name)
    def weeklyPay(self, hours):
        pay = self.salary/52
        return pay

class Manager(SalariedEmployee):
    def __init__(self,name,salary, bonus):
        self.bonus = bonus
        super(Manager,self).__init__(name,salary)
    def weeklyPay(self, hours):
        x = super(Manager,self).weeklyPay(hours)
        pay = x + self.bonus
        return pay


#def main():
#    staff = []
#    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
#    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
#    staff.append(Manager("Smith, Mary", 104000.0, 50.0))
#    for employee in staff :
#        hours = int(input("Hours worked by " + employee.getName() + ": "))
#        pay = employee.weeklyPay(hours)
#        print("Salary: %.2f" % pay)
#if __name__ == '__main__':
#    main()