from Lab5.num_to_words.convertor import convertor

def welcome():
    return f"Вітаю, ця программа переводить чилсо в текст"

def num_2_words():
    num = int(input("Вітаю, введіть число для перетвореня в письмову форму: "))
    return convertor(num)


def main():
    welcome()
    num_2_words()

if __name__ == '__main__':
    main()