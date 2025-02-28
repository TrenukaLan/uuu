import function


def main():
    print("Доступные функции:")
    print("1. Угадайка")
    print("2. Волшебный шар")
    print("3. Посчитать сумму покупки")
    print("4. Конвертирование валют")
    print("5. Ваше приветствие")

    choice = input("Введите номер функции, которую хотите запустить (1-4): ")

    if choice == '1':
        function.guess()
    elif choice == '2':
        function.magicalball()
    elif choice == '3':
        function.tc()
    elif choice == '4':
        function.convert()
    else:
        print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")


main()
