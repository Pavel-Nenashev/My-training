import time
import hashlib
'''     Класс User:
    Обладает следующими атрибутами: nickname (имя пользователя, строка),
    password (в хэшированном виде, число), age (возраст, число)
'''
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

'''     Класс Video:
    Обладает следующими атрибутами: title (заголовок), duration (продолжительность),
    time_now (секунда остановки (изначально 0)), adult_mode(ограничение по возрасту,
    bool (False по умолчанию)).
'''
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

'''    Класс UrTube:
    Обладает следующими атрибутами: users (список объектов User), videos (список объектов Video),
    current_user(текущий пользователь, User) и содержит следующие методы: log_in, register,
    log_out, add, get_videos, watch_video.
'''
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    # Метод log_in ищет пользователя в users с определенным nickname и password, и
    # меняет current_user на найденного (user), если такой пользователь существует.
    def log_in(self, nickname, password):
        # Создаем дополнительную переменную hashed_password для сравнения пароля,
        # который передается в виде строки, а сравнивается по хэшу.
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return

        print("Пользователь не найден!")

    # Метод register, с аргументами nickname, password, age добавляет пользователя
    # в список (с таким же nickname), если пользователя не существует.
    # Если существует, выводит на экран: "Пользователь {nickname} уже существует".
    # После регистрации, вход выполняется автоматически.
    def register(self, nickname, password, age):

        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        # Вход после регистрации
        self.current_user = new_user

    # Метод log_out для сброса текущего пользователя на None.
    def log_out(self):
        self.current_user = None

    # Метод add принимает неограниченное кол-во объектов класса Video и все
    # добавляет в videos, если с таким же названием видео ещё не существует.
    # В противном случае ничего не происходит.
    def add(self, *videos):

        for video in videos:
            if str(video) not in self.videos:
                self.videos.append(video)

    # Метод get_videos принимает поисковое слово и возвращает список названий
    # всех видео, содержащих поисковое слово(search_word).
    def get_videos(self, search_word):
        list_of_search = []

        for video in self.videos:
            if search_word.lower() in video.title.lower():
               list_of_search.append(video.title)
        return list_of_search

    # Метод watch_video принимает название фильма, если не находит
    # точного совпадения (вплоть до пробела), то ничего не воспроизводится,
    # если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
    # После текущее время просмотра данного видео сбрасывается.
    def watch_video(self, title):
        if not self.current_user:
            return print("Войдите в аккаунт, чтобы смотреть видео")

        for video in self.videos:

            if video.title == title:
                # Проверка возрастного ограничения
                if video.adult_mode and self.current_user.age < 18:
                    return print("Вам нет 18 лет, пожалуйста покиньте страницу")
                print(f"Воспроизводится: {video.title}")
                # Отсчет времени в консоль
                for i in range (video.time_now, video.duration):
                    print(f'Воспроизведено {i + 1} секунд')
                    time.sleep(1)
                print("Конец видео")
                # Сбросить текущее время просмотра
                video.time_now = 0
                return

        print("Видео не найдено.")

# Код для проверки работы классов
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # "Войдите в аккаунт..."
ur.register('vasya_pupkin', 'lolkekcheburek', 13)  # Регистрация пользователя
ur.watch_video('Для чего девушкам парень программист?')  # "Вам нет 18 лет..."
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Регистрация пользователя с доступом к видео
ur.watch_video('Для чего девушкам парень программист?')  # Просмотр видео

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Попытка зарегистрироваться с существующим никнеймом
print(ur.current_user.nickname)  # 'urban_pythonist'

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  # "Видео не найдено."









