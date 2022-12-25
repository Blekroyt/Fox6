#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from datetime import date

def get_worker():
    """
    Запросить данные о работнике.
    """
    name = input("Фамилия, Имя? ")
    tel = input("Номер телефона? ")
    date = int(input("Дата рождения? "))
    # Создать словарь.
    return {
    'name': name,
    'tel': post,
    'date   ': year,
    }

def display_workers(staff):
    """
    Отобразить список номеров.
    """
    # Проверить, что список номеров не пуст.
    if staff:
    # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)
    print(
    '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
    "No",
    "Ф.И.О.",
    "Номер",
    "Дата рожддения"
    )
    )
    print(line)
    # Вывести данные о всех номерах.
    for idx, worker in enumerate(staff, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
            idx,
            worker.get('name', ''),
            worker.get('tel', ''),
            worker.get('date', 0)
            )
            )
        print(line)
    else:
        print("Список номеров пуст.")

def select_workers(staff, period):
    """
    Выбрать номер с заданным годом рождения.
    """
    # Получить текущую дату.
    today = date.today()
    # Сформировать список номеров.
    result = []
    for employee in staff:
        if today.year - employee.get('year', today.year) >= period:
            result.append(employee)
    # Возвратить список выбранных номеров.
    return result

def save_workers(file_name, staff):
    """
    Сохранить все номера в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(staff, fout, ensure_ascii=False, indent=4)

def load_workers(file_name):
    """
    Загрузить все номера из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)

def main():
    """
    Главная функция программы.
    """
    # Список номеров.
    workers = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == "exit":
            break
        elif command == "add":
            # Запросить данные о номере.
            worker = get_worker()
            # Добавить словарь в список.
            workers.append(worker)
            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))
        elif command == "list":
            # Отобразить все номера.
            display_workers(workers)
        elif command.startswith("select "):
            # Разбить команду на части для выделения года.
            parts = command.split(maxsplit=1)
            # Получить требуемый год.
            period = int(parts[1])
            # Выбрать номера с заданным годом.
            selected = select_workers(workers, period)
            # Отобразить выбранные номера.
            display_workers(selected)
        elif command.startswith("save "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именемф.
            save_workers(file_name, workers)
        elif command.startswith("load "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именем.
            workers = load_workers(file_name)
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла;")
            print("save - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
    else:
        print(f"Неизвестная команда {command}", file=sys.stderr)

if __name__ == '__main__':
    main()
