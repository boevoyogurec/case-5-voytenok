import csv
import os

def process_csv_to_txt(input_file, output_file):
    # Считаем количество строк в CSV файле
    with open(input_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)  # Читаем все строки в список
        row_count = len(rows)  # Подсчитываем количество строк

    # Записываем результат в TXT файл
    with open(output_file, mode='w') as file:
        file.write(f"Количество строк в таблице: {row_count}\n")
        for row in rows:
            file.write(', '.join(row) + '\n')  # Записываем каждую строку

    return output_file

# Указываем путь к файлам
input_csv_path = os.path.join('data', 'weekly_IBM.csv')
output_txt_path = os.path.join('data', 'output.txt')


