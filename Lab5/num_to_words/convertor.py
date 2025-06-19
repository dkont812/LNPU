from num2words import num2words
def convertor(conv):

    try:
        return num2words(conv, lang='uk')
    except Exception as e:
        return f"Помилка"
