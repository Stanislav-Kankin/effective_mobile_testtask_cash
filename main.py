class Wallet:
    """
    Класс для учета личных доходов и расходов.
    """

    def __init__(self, filename) -> None:
        """
        Инициализирует объект Wallet с указанным именем файла.

        Args:
            filename (str): Имя файла для хранения записей.
        """
        self.filename = filename
        self.records = []
        self.load_records()

    def load_records(self) -> None:
        """
        Загружает записи из файла в список self.records.
        """
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    record = line.strip().split(',')
                    if len(record) == 5:
                        date, category, amount, currency, description = record
                        self.records.append({
                            'date': date,
                            'category': category,
                            'amount': float(amount),
                            'currency': currency,
                            'description': description
                        })
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден. Будет создан новый файл.")

    def save_records(self) -> None:
        """
        Сохраняет записи из списка self.records в файл.
        """
        with open(self.filename, 'w') as file:
            for record in self.records:
                line = ','.join([
                    record['date'],
                    record['category'],
                    str(record['amount']),
                    record['currency'],
                    record['description']
                ])
                file.write(line + '\n')

    def show_balance(self) -> None:
        """
        Выводит текущий баланс, а также отдельно доходы и расходы.
        """
        income = sum(record['amount'] for record in self.records if record['category'] == 'income')
        expense = sum(record['amount'] for record in self.records if record['category'] == 'expense')
        balance = income - expense
        print(f"Баланс: {balance:.2f}")
        print(f"Доходы: {income:.2f}")
        print(f"Расходы: {expense:.2f}")

    def add_record(self) -> None:
        """
        Добавляет новую запись о доходе или расходе.
        """
        date = input("Введите дату (ГГГГ-ММ-ДД): ")
        category = input("Введите категорию (income/expense): ")
        amount = float(input("Введите сумму: "))
        currency = input("Введите валюту: ")
        description = input("Введите описание: ")

        record = {
            'date': date,
            'category': category,
            'amount': amount,
            'currency': currency,
            'description': description
        }

        self.records.append(record)
        self.save_records()
        print("Запись успешно добавлена.")
