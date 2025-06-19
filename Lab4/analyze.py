
def analyze(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Шлях до файла вказаний не вірно, чи файла не існує")
        return

    total = len(lines)
    empty = sum(1 for line in lines if line.strip() == "")
    z_lines = sum(1 for line in lines if 'z' in line)
    z_count = sum(line.count('z') for line in lines)
    and_count = sum(1 for line in lines if 'and' in line)
    print(f"Загальна кількість рядків: {total}")
    print(f"Кількість пустих рядків: {empty}")
    print(f"Кількість рядків з літерою 'z': {z_lines}")
    print(f"Кількість літер 'z': {z_count}")
    print(f"Кількість рядків з 'and': {and_count}")
