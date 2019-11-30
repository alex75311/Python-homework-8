'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
'''


class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def extractor(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def valid(date_int):
        day, month, year = Date.extractor(date_int)
        if year <= 1900 or year >= 2099 or month < 1 or month > 12 or day > 31 or day < 1:
            return print('Не верная дата')
        # elif 1 > month > 12:
        #     return print('Не верная дата')
        elif month in (2, 4, 6, 9, 11) and day > 30:
            return print('Не верная дата')
        else:
            return print('Верная дата')


print(Date.extractor('15-58-648'))
Date.valid('31-05-2019')
Date.valid('31-04-2019')
Date.valid('32-11-2019')
Date.valid('0-01-2019')
