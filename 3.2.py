def send_email(message, recipient, *, sender = "university.help@gmail.com"):

    # Проверка на корректность e-mail отправителя и получателя
    valid_domains = (".com", ".ru", ".net")

    if not sender.endswith(valid_domains) or not recipient.endswith(valid_domains):
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if "@" not in recipient or not sender:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    # Проверка на отправку самому себе
    if sender == recipient:
        return print("Нельзя отправить письмо самому себе!")

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        return print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        return print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

    #Пример выполняемого кода(тесты):
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

send_email('Hello World', 'example@mail.ru', sender='example@mail.su')
send_email('Здесь вам не тут!!!', 'examplemail.ru', sender='example@mail.ru')
send_email('Галя у нас отмена', 'example@mail.ru')
send_email('Теперь Вы понимаете всю глубину наших глубин?', 'example@mail.ru', sender='urban.info@gmail.com')
send_email('Just do it.', 'na_vse_100@crabca.com', sender='university.help@gmail.com')
