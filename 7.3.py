class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    # get_all_words - подготовительный метод, который возвращает словарь с названиями файлов
    # и списками слов из них
    def get_all_words(self):
        all_words = {}                                              # Создаем пустой словарь
        delete_chars = [',', '.', '=', '!', '?', ';', ':', ' - ']   # Задаем список символов для удаления
        for file in self.file_names:                                # Перебираем список файлов
            with open(file, 'r', encoding='utf-8') as f:            # Открываем файлы для чтения
                text = f.read().lower()                             # Переводим содержимое в нижний регистр
                for char in delete_chars:
                    text = text.replace(char, '')             # Заменяем удаляемые символы на пробелы
                words = text.split()                                # Разбиваем текст на слова по пробелам
                all_words.update({file: words})                     # Заполняем словарь
        return all_words

    # Возвращает словарь, где ключ - название файла, значение - позиция первого
    # такого слова в списке слов этого файла.
    def find(self, word):
        word = word.lower()
        find_dict = {}
        for name, words in self.get_all_words().items():
            cnt = 1
            for w in words:
                if w == word:
                    find_dict[name] = cnt
                    break
                cnt += 1
        return find_dict

    # Возвращает словарь, где ключ - название файла, значение - количество слов
    # word в списке слов этого файла.
    def count(self, word):
        word = word.lower()
        count_dict = {}
        for name, words in self.get_all_words().items():
            cnt = 0
            for w in words:
                if w == word:
                    cnt += 1
            count_dict[name] = cnt
        return count_dict

    '''Примеры выполняемого кода:'''

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))