# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_func():
    user_list = input('Введите строку чисел разделенных пробелом, для выхода из программы введите "q":\n')
    num_list = []

    def re_list(func_list):
        func_list = func_list.split()
        for el in func_list[::]:
            if el.isdigit():
                func_list.pop(func_list.index(el))
                num_list.append(int(el))
            if not el.isdigit():
                if el == "q":
                    func_list.pop(func_list.index(el))
                    print(f'Сумма списка {num_list} = {sum(num_list)}\nПрограмма завершена.')
                    return 1
                else:
                    print(f"Удален элемент '{func_list.pop(func_list.index(el))}' т.к. не является числом")

        print(f'Сумма списка {num_list} = {sum(num_list)}')

    if re_list(user_list) == 1:
        return
    while True:
        user_list_1 = input('Введите строку чисел разделенных пробелом:\n')
        if re_list(user_list_1) == 1:
            return


my_func()
