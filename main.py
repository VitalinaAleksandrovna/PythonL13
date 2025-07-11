# Задача 1
# Реализовать программу для вывода
# последовательности чисел Фибоначчи до определённого
# числа в последовательности. Номер числа, до которого нужно
# выводить, задаётся пользователем с клавиатуры. Для
# реализация последовательности использовать генераторную
# функция.

def fibonacci_generator(max_count):
    a, b = 0, 1
    count = 0
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1


def main():
    try:
        n = int(input("Введите количество чисел Фибоначчи для вывода: "))
        if n <= 0:
            print("Пожалуйста, введите положительное число")
            return

        print(f"Первые {n} чисел последовательности Фибоначчи:")
        for num in fibonacci_generator(n):
            print(num, end=" ")
        print()

    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == "__main__":
    main()