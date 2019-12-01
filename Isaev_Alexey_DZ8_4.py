'''
1. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
2. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
3. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''

from abc import ABC, abstractmethod


class Department(ABC):

    @abstractmethod
    def add(self, type_technic, data):
        pass


class MyTypeError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Storage:

    def __init__(self):
        self.__storage = {}

    @property
    def storage(self):
        return self.__storage

    def add_technic(self, technic, number):
        try:
            if not isinstance(number, int):
                raise MyTypeError('type of number must be int')
            technic.params['number'] = number
            if not self.__storage.get(technic.type_technic):
                self.__storage[technic.type_technic] = {technic.name: technic.params}
            else:
                self.__storage[technic.type_technic].setdefault(technic.name, technic.params)
        except MyTypeError as e:
            print(e)

    def transfer_to_department(self, technic, department):
        department.add(technic.type_technic, self.__storage.get(technic.type_technic))


class TransportDepartment(Department):

    def __init__(self):
        self.__storage = {}

    @property
    def storage(self):
        return self.__storage

    def add(self, type_technic, data):
        if not self.__storage.get(type_technic):
            self.__storage[type_technic] = data
        else:
            self.__storage[type_technic].setdefault(data)


class OfficeTechnics:

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


class Printer(OfficeTechnics):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color)
        self.type_technic = self.__class__.__name__
        self.print_speed = speed
        self.params = {'name': self.name, 'color': self.color, 'print_speed': self.print_speed}


class Scanner(OfficeTechnics):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color)
        self.type_technic = self.__class__.__name__
        self.scan_speed = speed
        self.params = {'name': self.name, 'color': self.color, 'scan_speed': self.scan_speed}


class Copier(OfficeTechnics):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color)
        self.type_technic = self.__class__.__name__
        self.copy_speed = speed
        self.params = {'name': self.name, 'color': self.color, 'copy_speed': self.copy_speed}


if __name__ == '__main__':
    printer = Printer('HP', 'Black', 12)
    scaner = Scanner('Canon', 'White', 15)
    copier = Copier('Canon', 'Gray', 23)
    print(f'printer: {printer}')
    print(f'scaner: {scaner}')
    print(f'copier: {copier}')
    storage = Storage()
    storage.add_technic(printer, 20)
    storage.add_technic(scaner, 50)
    print(f'storage: {storage.storage}')
    transportDep = TransportDepartment()
    storage.transfer_to_department(scaner, transportDep)
    print(f'transportDep storage: {transportDep.storage}')
