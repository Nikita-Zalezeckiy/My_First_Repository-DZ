
import csv

columns = ('ID in Programma', 'Name/Niki', 'Position')
data = []

with open('Programma.csv', 'w') as file:

        file.write(','.join(columns) + '\n') # объединение кортежа в строку для записи в БД

        for line in data:
            line = [str(i) for i in line] # переводим элементы списка в str
            file.write(','.join(line) + '\n') # объединение кортежа в строку
print(columns, data)

def write_to_data_base(filename):

    with open(filename, 'w') as file:

        file.write(','.join(columns) + '\n') # объединение кортежа в строку для записи в БД

        for line in data:
            line = [str(i) for i in line] # переводим элементы списка в str
            file.write(','.join(line) + '\n') # объединение кортежа в строку
    print(columns, data)

def read_from_data_base(filename):

    with open(filename, 'r') as file:

        columns = tuple(file.readline().split(','))
        data = []

        for line in file:
            line = tuple(line.split(','))
            data.append(line)

    print(columns, data)

    return columns, data

def get_line():

    new_line = tuple(input('Введите данные: ').split()) # создание кортежа данных
    if new_line not in data:
        data.append(new_line) # вставляю в конец списка из кортежей новый кортеж

# columns = ('ID in Programma', 'Name/Niki', 'Position')
# data = []

columns, data = read_from_data_base('Programma.csv')

get_line()

write_to_data_base('Programma.csv')
