import time
import getpass

# Хранение
transaction_history = []

# Значения Николая
login1 = 1
password1 = 1
name1 = 'Николай'
cart1 = 2200220022002200
balance1 = 1000


# Значения Евгения
login2 = 2
password2 = 2
name2 = 'Евгений'
cart2 = 5
balance2 = 20000

print('Вас приветствует программа SberBank')
print('Система авторизации')
Login_A = input('Введите ваш логин: ')
password = getpass.getpass('Введите ваш пароль: ')

if (password == '1' and Login_A == str(login1)) or (password == '2' and Login_A == str(login2)):
    print('Идет проверка. При положительном результате вы будете впущены в программу.')
else:
    print('Неверный логин или пароль.')



# Функционал
while True:
    print('0. Выйти из программы')
    print('1. Посмотреть баланс карточки')
    print('2. Перевести деньги на карту')
    print('3. Пополнение карточки')
    print('4. Оплатить налоги')
    print ('5. Оплатить за электричество')
    print("6. Оплатить налог за налог")
    cmd = input('Выберите пункт: ')

    # Логика
    if cmd == "0":
        print('Выбран пункт 0')
        break
    elif cmd == "1":
        if Login_A == str(login1):
            print(f'Баланс карточки {name1}: {balance1} рублей')
        elif Login_A == str(login2):
            print(f'Баланс карточки {name2}: {balance2} рублей')
    elif cmd == "2":
        cart_enter = input('Введите номер карты получателя: ')
        amount = float(input('Введите сумму для перевода: '))
        print(f'Вы ввели сумму для перевода: {amount}')
        
        if Login_A == str(login1):
            if amount > balance1:
                print('Ошибка: Недостаточно средств на счете.')
            else:
                reg = input('Вы уверены, что хотите совершить перевод? (Да/Нет): ')
                if reg.lower() == 'да':
                    balance1 -= amount
                    print(f'Перевод успешно выполнен. Остаток на счете: {balance1} рублей.')
                else:
                    print('Отмена перевода.')
        
        elif Login_A == str(login2):
            if amount > balance2:
                print('Ошибка: Недостаточно средств на счете.')
            else:
                reg = input('Вы уверены что хотите совершить перевод? (Да/Нет): ')
                if reg.lower() == 'да':
                    balance2 -= amount
                    print(f'Перевод успешно выполнен. Остаток на счете: {balance2} рублей.')
                else:
                    print('Отмена перевода.')

    elif cmd == "3":
        amount = float(input('Введите сумму для пополнения карточки: '))
        if amount > 0:
            if Login_A == str(login1):
                balance1 += amount
                print(f'Карточка {name1} успешно пополнена на {amount} рублей. Остаток на счете: {balance1} рублей.')
            elif Login_A == str(login2):
                balance2 += amount
                print(f'Карточка {name2} успешно пополнена на {amount} рублей. Остаток на счете: {balance2} рублей.')
        else:
            print('Ошибка: Введите положительное значение для пополнения.')

    elif cmd == "4":
        tax_amount = float(input('Введите сумму налогового платежа: '))
        if Login_A == str(login1):
            if tax_amount > balance1:
                print('Ошибка: Недостаточно средств на счете для оплаты налогов.')
            else:
                balance1 -= tax_amount
                print(f'Налоговый платеж в размере {tax_amount} рублей успешно оплачен.')
        elif Login_A == str(login2):
            if tax_amount > balance2:
                print('Ошибка: Недостаточно средств на счете для оплаты налогов.')
            else:
                balance2 -= tax_amount
                print(f'Налоговый платеж в размере {tax_amount} рублей успешно оплачен.')

if cmd == "5":
    electricity_amount = float(input('Введите сумму оплаты за электричество: '))
    if Login_A == str(login1):
        if electricity_amount > balance1:
            print('Ошибка: Недостаточно средств на счете для оплаты за электричество.')
        else:
            balance1 -= electricity_amount
            print(f'Оплата за электричество на сумму {electricity_amount} рублей выполнена.')
            tax_amount = 0.1 * electricity_amount
            print(f'Оплата налога за электричество в размере {tax_amount} рублей выполнена.')
    elif Login_A == str(login2):
        if electricity_amount > balance2:
            print('Ошибка: Недостаточно средств на счете для оплаты за электричество.')
        else:
            balance2 -= electricity_amount
            print(f'Оплата за электричество на сумму {electricity_amount} рублей выполнена.')
            tax_amount = 0.1 * electricity_amount 
            print(f'Оплата налога за электричество в размере {tax_amount} рублей выполнена.')


    elif cmd == "6":
        tax_amount = float(input('Введите сумму налога за налог: '))
    if Login_A == str(login1):
        if tax_amount > balance1:
            print('Ошибка: Недостаточно средств на счете для оплаты налога за налог.')
        else:
            balance1 -= tax_amount
            print(f'Оплата налога за налог на сумму {tax_amount} рублей выполнена.')
    elif Login_A == str(login2):
        if tax_amount > balance2:
            print('Ошибка: Недостаточно средств на счете для оплаты налога за налог.')
        else:
            balance2 -= tax_amount
            print(f'Оплата налога за налог на сумму {tax_amount} рублей выполнена.')
            
   
            