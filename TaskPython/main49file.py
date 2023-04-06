# Создать телефонный справочник с возможностью 
# импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, 
# которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик
# для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def read_file():
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line.strip())

def write_file():
    with open(file_path, 'a', encoding='UTF-8') as f:
        f.writelines('\n' + input('Введите запись: '))

def find_file():
    find_info = input('Поиск: ')
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)


def main():
    find_file()


file_path = r'phone_book.txt'
main()
