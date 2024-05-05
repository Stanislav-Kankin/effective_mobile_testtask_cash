class Wallet:
    """
    Класс для учета личных доходов и расходов.
    """

    def __init__(self, filename):
        """
        Инициализирует объект Wallet с указанным именем файла.

        Args:
            filename (str): Имя файла для хранения записей.
        """
        self.filename = filename
        self.records = []
        self.load_records()

    def load_records(self):
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