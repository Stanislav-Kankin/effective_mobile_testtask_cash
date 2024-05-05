import unittest
from unittest.mock import patch, mock_open
from io import StringIO

from main import Wallet


class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet('test_records.txt')

    def tearDown(self):
        try:
            import os
            os.remove('test_records.txt')
        except:
            pass

    def test_load_records(self):
        with patch('builtins.open', mock_open(read_data='Дата: 2023-05-01\nКатегория: Доход\nСумма: 1000.0\nОписание: Зарплата\n\nДата: 2023-05-02\nКатегория: Расход\nСумма: 500.0\nОписание: Аренда\n\n')):
            self.wallet.load_records()
            self.assertEqual(len(self.wallet.records), 2)
            self.assertEqual(self.wallet.records[0]['date'], '2023-05-01')
            self.assertEqual(self.wallet.records[0]['category'], 'income')
            self.assertEqual(self.wallet.records[0]['amount'], 1000.0)
            self.assertEqual(self.wallet.records[0]['description'], 'Зарплата')

    def test_add_record(self):
        with patch('builtins.input', side_effect=['2023-05-03', 'income', '2000', 'Бонус']):
            self.wallet.add_record()
            self.assertEqual(len(self.wallet.records), 1)
            self.assertEqual(self.wallet.records[0]['date'], '2023-05-03')
            self.assertEqual(self.wallet.records[0]['category'], 'income')
            self.assertEqual(self.wallet.records[0]['amount'], 2000.0)
            self.assertEqual(self.wallet.records[0]['description'], 'Бонус')

    def test_edit_record(self):
        self.wallet.records = [
            {'date': '2023-05-01', 'category': 'income', 'amount': 1000.0, 'description': 'Зарплата'},
            {'date': '2023-05-02', 'category': 'expense', 'amount': 500.0, 'description': 'Аренда'}
        ]
        with patch('builtins.input', side_effect=['0', '', '', '', '2023-05-01', 'Доход обновленный']):
            self.wallet.edit_record()
            self.assertEqual(self.wallet.records[0]['date'], '2023-05-01')
            self.assertEqual(self.wallet.records[0]['category'], 'income')
            self.assertEqual(self.wallet.records[0]['amount'], 1000.0)
            self.assertEqual(self.wallet.records[0]['description'], '2023-05-01')

    def test_search_records(self):
        self.wallet.records = [
            {'date': '2023-05-01', 'category': 'income', 'amount': 1000.0, 'description': 'Зарплата'},
            {'date': '2023-05-02', 'category': 'expense', 'amount': 500.0, 'description': 'Аренда'},
            {'date': '2023-05-03', 'category': 'income', 'amount': 2000.0, 'description': 'Бонус'}
        ]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.wallet.search_records()
            output = fake_out.getvalue().strip()
            expected_output = "Найденные записи:\n2023-05-01, income, 1000.0, Зарплата\n2023-05-03, income, 2000.0, Бонус"
            self.assertEqual(output, expected_output)

    def test_delete_record(self):
        self.wallet.records = [
            {'date': '2023-05-01', 'category': 'income', 'amount': 1000.0, 'description': 'Зарплата'},
            {'date': '2023-05-02', 'category': 'expense', 'amount': 500.0, 'description': 'Аренда'},
            {'date': '2023-05-03', 'category': 'income', 'amount': 2000.0, 'description': 'Бонус'}
        ]
        with patch('builtins.input', return_value='1'):
            self.wallet.delete_record()
            self.assertEqual(len(self.wallet.records), 2)
            self.assertEqual(self.wallet.records[0]['date'], '2023-05-01')
            self.assertEqual(self.wallet.records[1]['date'], '2023-05-03')


if __name__ == '__main__':
    unittest.main()
