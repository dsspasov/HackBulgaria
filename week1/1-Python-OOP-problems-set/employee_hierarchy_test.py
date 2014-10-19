#employee_hierarchy_test.py

import unittest
from employee_hierarchy import *

class TestEmployeeHierarchy(unittest.TestCase):

    def setUp(self):
        self.emolyee = Employee('test')
        self.hourly_employee = HourlyEmployee('test', 10)
        self.salaried_employee = SalariedEmployee('test', 1040.0)
        self.manager = Manager('test', 1040.0 , 2)
    def tearUp(self):
        pass
    def test_Employee_get_name(self):
        self.assertEqual('test',self.emolyee.getName())
    def test_HourlyEmployee_WeeklyPay(self):
        self.assertEqual(0,self.hourly_employee.weeklyPay(-5))
        self.assertEqual(20,self.hourly_employee.weeklyPay(2))
        self.assertEqual(415,self.hourly_employee.weeklyPay(41))
    def test_SalariedEmployee_WeeklyPay(self):
        self.assertEqual(20.0,self.salaried_employee.weeklyPay(2))
    def test_ManagerWeeklyPay(self):
        self.assertEqual(22.0,self.manager.weeklyPay(10))



if __name__ == '__main__':
    unittest.main()
