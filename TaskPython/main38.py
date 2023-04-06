# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

def change_file():
    find_info = input('Поиск: ')
    new_info = input('Введите исправление: ')
    with open(file_path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    with open(file_path, 'w', encoding='UTF-8') as f:
        for line in lines:
            if find_info.casefold() in line.casefold():
                print(line)
                if input('Да/Нет: ') == 'Да':
                    lst = (line.strip()).split(' ')
                    for i in range(len(lst)):
                        if lst[i].casefold() == find_info.casefold():
                            lst[i] = new_info
                    line = ' '.join(lst)
                    f.write(line + '\n')
                else:
                    f.write(line)
            else:
                f.write(line)
    
def del_from_file():
    find_del = input('Удалить: ')
    with open(file_path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    with open(file_path, 'w', encoding='UTF-8') as f:
        for line in lines:
            if find_del.casefold() in line.casefold():
                print(line)
                if input('Да/Нет: ') == 'Да':
                    continue
                else:
                    f.write(line)
            else:
                f.write(line)



def main():
    del_from_file()


file_path = r'phone_book.txt'
main()
