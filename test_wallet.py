import unittest
from io import StringIO
from unittest.mock import patch

from main import Wallet


class TestFinancialWallet(unittest.TestCase):
    def setUp(self) -> None:
        self.wallet = Wallet('test_records.txt')

    def test_load_records(self):
        self.wallet.records = []
        self.wallet.load_records()
        self.assertEqual(len(self.wallet.records), 2)
        self.assertEqual(self.wallet.records[0]['date'], '2024-05-02')
        self.assertEqual(self.wallet.records[0]['category'], 'expense')
        self.assertEqual(self.wallet.records[0]['amount'], 1500.0)
        self.assertEqual(self.wallet.records[0]['currency'], 'USD')
        self.assertEqual(self.wallet.records[0]['description'], 'Покупка продуктов')

    def test_show_balance(self) -> None:
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.wallet.show_balance()
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "Баланс: 28500.00\nДоходы: 30000.00\nРасходы: 1500.00")

    def test_add_record(self) -> None:
        with patch('builtins.input', side_effect=['2024-06-01', 'income', '5000', 'USD', 'Зарплата']):
            self.wallet.add_record()
            self.assertEqual(len(self.wallet.records), 3)
            self.assertEqual(self.wallet.records[-1]['date'], '2024-06-01')
            self.assertEqual(self.wallet.records[-1]['category'], 'income')
            self.assertEqual(self.wallet.records[-1]['amount'], 5000.0)
            self.assertEqual(self.wallet.records[-1]['currency'], 'USD')
            self.assertEqual(self.wallet.records[-1]['description'], 'Зарплата')

    def test_edit_record(self) -> None:
        with patch('builtins.input', side_effect=['0', '', '', '', 'Покупка продуктов питания']):
            self.wallet.edit_record()
            self.assertEqual(self.wallet.records[0]['description'], 'Покупка продуктов питания')

    def test_search_records(self) -> None:
        with patch('builtins.input', side_effect=['income', '', '']):
            self.wallet.search_records()
            # Проверка вывода для найденных записей


if __name__ == '__main__':
    unittest.main()
