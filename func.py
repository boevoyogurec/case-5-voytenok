import csv
import os

def process_csv_to_txt(input_file, output_file):
    # Считаем количество строк в CSV файле
    with open(input_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)  # Читаем все строки в список
        row_count = len(rows)  # Подсчитываем количество строк

