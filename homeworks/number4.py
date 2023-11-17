def menu(operation):
    match operation:
        case 'save':
            print('Сохранить')
        case 'load':
            print('Загрузить')
        case _:
            print('Неизвестная операция')
menu((input('Введите операцию: ')))