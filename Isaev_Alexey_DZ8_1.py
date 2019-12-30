'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
'''


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extractor(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def valid(date_int):
        day, month, year = Date.extractor(date_int)
        if 2099 >= year <= 1900 or 12 > month < 1 or 1 > day > 31:
            return print('Не верная дата')
        elif month in (4, 6, 9, 11) and day > 30:
            return print('Не верная дата')
        elif (year % 400 != 0 and (year % 4 != 0 and year % 100 != 0)) and month == 2 and day > 28:
            return print('Не верная дата')
        else:
            return print('Верная дата')


print(Date.extractor('15-12-2019'))
Date.valid('31-05-1019')
Date.valid('31-04-3019')
Date.valid('32-11-2019')
Date.valid('28-02-2013')
Date.valid('29-02-2013')
Date.valid('29-02-2008')
Date.valid('31-01-2008')
Date.valid('15-01-2019')
