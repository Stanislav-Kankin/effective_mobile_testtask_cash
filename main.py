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

    def edit_record(self) -> None:
        """
        Изменяет существующую запись о доходе или расходе.
        """
        index = int(input("Введите индекс записи для редактирования: "))
        if index < 0 or index >= len(self.records):
            print("Неверный индекс записи.")
            return

        record = self.records[index]
        date = input(f"Введите новую дату ({record['date']}) или нажмите Enter для пропуска: ")
        category = input(f"Введите новую категорию ({record['category']}) или нажмите Enter для пропуска: ")
        amount = input(f"Введите новую сумму ({record['amount']}) или нажмите Enter для пропуска: ")
        currency = input(f"Введите новую валюту ({record['currency']}) или нажмите Enter для пропуска: ")
        description = input(f"Введите новое описание ({record['description']}) или нажмите Enter для пропуска: ")

        if date:
            record['date'] = date
        if category:
            record['category'] = category
        if amount:
            record['amount'] = float(amount)
        if currency:
            record['currency'] = currency
        if description:
            record['description'] = description

        self.save_records()
        print("Запись успешно обновлена.")


def search_records(self) -> None:
        """
        Производит поиск записей по категории, дате или сумме.
        """
        search_category = input("Введите категорию для поиска (income/expense) или нажмите Enter для пропуска: ")
        search_date = input("Введите дату для поиска (ГГГГ-ММ-ДД) или нажмите Enter для пропуска: ")
        search_amount = input("Введите сумму для поиска или нажмите Enter для пропуска: ")

        matching_records = []
        for record in self.records:
            if (not search_category or record['category'] == search_category) and \
               (not search_date or record['date'] == search_date) and \
               (not search_amount or record['amount'] == float(search_amount)):
                matching_records.append(record)

        if matching_records:
            print("Найденные записи:")
            for record in matching_records:
                print(f"{record['date']}, {record['category']}, {record['amount']}, {record['currency']}, {record['description']}")
        else:
            print("Записи не найдены.")


def main() -> None:
    """
    Главная функция для запуска приложения.
    """
    wallet = Wallet('records.txt')

    while True:
        print("\nВыберите действие:")
        print("1. Вывод баланса")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск по записям")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            wallet.show_balance()
        elif choice == '2':
            wallet.add_record()
        elif choice == '3':
            wallet.edit_record()
        elif choice == '4':
            wallet.search_records()
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
