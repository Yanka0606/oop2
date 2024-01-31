def strings_count(file):  # Функция подсчета строк в файле
    with open(file, encoding='utf-8') as file:
        return len(file.readlines())


# Файлы расположены в той же директории, что файл исполняемый файл
list_of_files = ['1.txt', '2.txt', '3.txt']
dict_of_files = {}  # Словарь с именами файлов и количеством строк
sorted_list_of_files = []  # Сортированный список из словаря

for name in list_of_files:
    dict_of_files[name] = strings_count(name)
sorted_list_of_files = sorted(dict_of_files.items(), key=lambda x: x[1])

with open('result_file.txt', 'w') as f4:
    for i in sorted_list_of_files:
        f4.write(i[0] + '\n')  # Первая строка
        f4.write(str(i[1]) + '\n')  # Вторая строка
        with open(i[0], encoding='utf-8') as f:  # Открываем нужный файл и пишем его содержимое в result_file.txt
            f4.write(f.read() + '\n')