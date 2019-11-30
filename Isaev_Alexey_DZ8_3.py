'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список. Класс-исключение должен
контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и
строки. При вводе пользователем очередного элемента необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
'''


class IntException(Exception):
    def __init__(self):
        self.txt = 'Введено не число '


res_list = []
while True:
    inp_user = input('Введите число или Enter для выхода ')
    if inp_user == '':
        break
    else:
        try:
            if inp_user.isdigit():
                res_list.append(int(inp_user))
            elif inp_user.count('.') > 1:
                raise IntException
            else:
                for sym in inp_user:
                    if not sym.isdigit() and sym != '.':
                        raise IntException
                res_list.append(float(inp_user))
        except IntException as err:
            print(err.txt)

print(res_list)
