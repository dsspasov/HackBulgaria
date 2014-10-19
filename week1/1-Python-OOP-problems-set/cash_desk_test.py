#cash_desk_test.py
import unittest
from cash_desk import CashDesk

class TestCashDesk(unittest.TestCase):
    def setUp(self):
        self.my_cash_desk = CashDesk()
    def test_total_zero_when_new_instance_made(self):
        self.assertEqual(0,self.my_cash_desk.total())
    def test_total_after_money_take(self):
        self.my_cash_desk.take_money({1:2,100:3})
        self.assertEqual(302, self.my_cash_desk.total())
    def test_can_withdraw_money_all_money(self):
        self.my_cash_desk.take_money({1: 2, 100: 3})
        self.assertTrue(self.my_cash_desk.can_withdraw_money(302))
    #def test_can_withdraw_money_not_all_money(self):
    #    self.my_cash_desk.take_money({1: 2, 100: 3})
    #    self.assertTrue(self.my_cash_desk.can_withdraw_money(202))

    def test_can_withdraw_money_cant_withdraw(self):
        self.my_cash_desk = CashDesk()
        self.my_cash_desk.take_money({1: 2, 100: 3})
        self.assertFalse(self.my_cash_desk.can_withdraw_money(105))

if __name__ == '__main__':
    unittest.main()
