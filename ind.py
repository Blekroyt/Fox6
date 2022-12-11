#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from datetime import date


def add():
    # Запросить данные .
    name = input("Фамилия, Имя ")
    tel = input("Номер телефона ")
    date = input("Дата рождения ")

    # Создать словарь.
    spisok = {"name": name, "tel": tel, "date": date}

    # Добавить словарь в список.
    spisoks.append(spisok)
    # Отсортировать список в случае необходимости.
    if len(spisok) > 1:
        spisoks.sort(key=lambda item: item.get("tel", ""))


def list():
    # Заголовок таблицы.
    line = "+-{}-+-{}-+-{}-+".format("-" * 30, "-" * 20, "-" * 14)
    print(line)
    print(
        "| {:^30} | {:^20} | {:^14} |".format(
            "Фамилия, Имя",
            "Номер телефона",
            "Дата рождения",
        )
    )
    print(line)

    # Вывести данные о всех людях.
    for idx, product in enumerate(spisoks, 1):
        print(
            "| {:<30} | {:<20} | {:>14} |".format(
                product.get("name", ""), product.get("tel", ""), product.get("date", 0)
            )
        )

    print(line)


def select():
    parts = command.split(" ", maxsplit=2)
    sel = parts[1]

    count = 0
    for spisok in spisoks:
        if spisok.get("name") == sel:
            count = "Дата рождения"
            print("{:>4}: {}".format(count, spisok.get("date", "")))
            print("Номер телефона", spisok.get("tel", ""))
            print("Фамилия Имя", spisok.get("name", ""))

    # Если счетчик равен 0, то рейсы не найдены.
    if count == 0:
        print("Люди не найден.")


def select_workers(staff, period):
    """
    Выбрать людей с заданным номером.
    """
    # Получить текущую дату.
    today = date.today()
    # Сформировать список работников.
    result = []
    for employee in staff:
        if today.year - employee.get("year", today.year) >= period:
            result.append(employee)
    # Возвратить список выбранных работников.
    return result


def save_workers(file_name, staff):
    """
    Сохранить всех людей в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить человека;")
    print("list - вывести список людей;")
    print("select <товар> - информация о человеке;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

    # Список .


spisoks = []

# Организовать бесконечный цикл запроса команд.
while True:
    # Запросить команду из терминала.
    command = input(
        ">>>>>>",
    ).lower()

    # Выполнить действие в соответствие с командой.
    if command == "exit":
        break

    elif command == "add":
        add()
    elif command == "list":
        list()

    elif command.startswith("select "):
        select()

    elif command == "help":
        help()
    else:
        print("Неизвестная команда {command}", file=sys.stderr)
        
if __name__ == "__main__":
    main()
