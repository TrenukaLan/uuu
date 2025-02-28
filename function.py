import random

def guess():
    s = random.randint(1, 100)
    a = 5
    print("Робот загадал число от 1 до 100.")

    for i in range(a):
        print("Попытка", str(i + 1), "из", a)
        g = int(input("Введите ваше число: "))

        if g < s:
            print("Загаданное число больше.")
        elif g > s:
            print("Загаданное число меньше.")
        else:
            print("Поздравляем! Вы угадали число", str(s), "!")
            break
    else:
        print("Попытки закончились. Загаданное число было", str(s), ".")


def magicalball():
    answers = [
        'Это точно!', 'Разумеется!', 'Да.', 'Так и есть.', 'Попробуйте другой вариант.',
        'Возможно.', 'Скорее всего, да.', 'Скорее всего, нет.', 'В другой раз.', 'Бесспорнно да.',
        'Лучше отложить решение.', 'Точно нет!', 'Никогда.', 'Даже не думайте!', 'Лучше не стоит.',
        'Подумайте сами.', 'Вы уверены, что вам это нужно?', 'Подумайте еще раз.', 'Нет.', 'Взвесьте все "за" и "против"',
    ]
    name = input("Привет, я Магический шар! А вас как зовут? ")
    print("Привет,", name + "!", "Я помогу вам с ответом на ваш вопрос!")

    while True:
        question = input("Задайте ваш вопрос: ")
        answer = random.choice(answers)
        print("Магический шар говорит:", answer)


def tc():
    total = 0
    while True:
        amount = input("Введите сумму покупки (или 'выход' для завершения): ")
        if amount.lower() == 'выход':
            break
        total += float(amount)
        print("Текущая общая сумма:", total)
    return total
    print("Итоговая сумма покупок:", total)

def convert():
    btc = 7113814.56
    eur = 91.75
    usd = 88.34

    rub = float(input("Введите количество рублей: "))
    print(rub, "RUB =", rub / btc, "BTC")
    print(rub, "RUB =", rub / eur, "EUR")
    print(rub, "RUB =", rub / usd, "USD")
