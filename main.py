#Реализовать программу(несколько функций) цензор.
#Принимает файл с текстом и список слов.
#На выходе:
#1) новый файл с тем же текстом, но заданные слова заменены на звездочки,
#2) файл stat.json(формат данных JSON) со статисткой(обновляемый) в виде:
#название файла, список слов, сколько раз каждое слово встретилось в тесте.
#3)файл stat.csv(формат данных csv) со статисткой(обновляемый) в виде:
#название файла, список слов, сколько раз каждое слово встретилось в тесте.

def censor(filename, some : list):
    # Открываем файл
    with open(filename, 'r') as file:
        data = file.readlines()
    #Создаем словарь с запрещенными словами
    dictionary = dict.fromkeys(some, 0)
    # Проходим циклом по списку
    for n in data:
        # Проходим циклом по списку запрещенных слов
        for i in some:
            while i in n.lower():
                lower_text = n.lower()
                finder = lower_text.find(i)
                counter = len(i)
                replace = "*" * counter
                find_index = data.index(n)
                n = n[:finder] + replace + n[finder + counter:]
                data[find_index] = n
                dictionary[i] += 1

    # Создаем новую строку
    new_str = ""
    for s in data:
        new_str += s
    # Создаем новый файл и записываем в него новую строку
    with open("new_text.txt", 'w') as file:
        file.write(new_str)
    return dictionary

#------------------------------------------------------------------------------------------------------------

import csv
import json
import homework10censor

# Список запрещенных слов
some_list: list[str] = ['nails', 'good', "buy", "flowers", "cry"]

# Функция для создания JSON
def json_creater():
    # Открываем доступ к файлу
    with open("stat.txt", "a") as file:
        json.dump(homework10censor('text.txt', some_list: list[str], file))

# Функция для создания CSV
def csv_creater():
    # Создаем список
    new_dict = []
    # Преобразование в список словарей
    for i in homework10censor.censor('text.txt', some_list: list[str]):
        new_dict.append({"word": i, "count": homework10censor.censor('text.txt', some_list: list[str]).get(i)})

    # Открываем доступ к файлу
    with open("stat.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["word", "count"])
        writer.writeheader()
        writer.writerows(new_dict)

json_creater()
csv_creater()




