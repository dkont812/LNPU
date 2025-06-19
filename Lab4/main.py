from analyze import *

def main():
    while True:
        path = input(f"Напишіть шлях до файлу: ").strip()
        analyze(path)

        repeat = input(f"Якщо треба проаналізувати ще один файл напишіть (y or yes), в іншому випадку напишіть (n or no):  ").strip()
        if repeat == "n":
            print(f"Програму завершено")
            break



if __name__ == '__main__':
    main()