from multiprocessing import Pool
import time

def read_info(name):
    all_data =[]                            # Создаем список
    with open(name, 'r') as file:           # Открываем файл для чтения
        while True:
            line = file.readline()          # Читаем файл построчно
            if line == '':                  # Если строка пустая
                break                       # Прерываем бесконечный цикл
            all_data.append(line.strip())   # Добавляем каждую строку в список all_data
    # return all_data


# Пример результата выполнения программы

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = time.time()
for files in filenames:
    read_info(files)
end_time = time.time()
print(f'Линейный вызов: {end_time - start_time:.6f} сек.')

# Многопроцессный подход
if __name__ =='__main__':
    start_time = time.time()
    with Pool(processes = len(filenames)) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f'Многопроцессный подход: {end_time - start_time:.6f} сек.')


