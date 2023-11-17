global_var = 10 # Глобальная переменная


def calculate_sum(param): # Параметр функции
    outer_var = 5 # Переменная из охватывающей области видимости

    def inner_function():
        nonlocal outer_var
        outer_var = 8
        local_var = 7 # Локальная переменная
        return global_var + outer_var + param + local_var

    return inner_function()


print(calculate_sum(10))
