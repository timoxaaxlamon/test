'''from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("My first Window")
#root.place(x=50, y=0)

label1 = Label(root, text="simple text:)", font="Arial 22")
label1.place(x=190, y=100)

label2 = Label(root, text="so more simple text", font="Consolas 15")
label2.place(x= 300, y=300)

okButton = Button(root, text="no any text", width="10", font="Consolas 15")
okButton.place(x=50, y=100)
root.mainloop()

#length = "40",'''
from typing import List

'''def check_query(query):
    tokens = query.split(',')
    print(tokens)
    return tokens[1]




# дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '-', result)

    sum'''

'''DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_query(query):
    tokens = query.split(', ')
    if tokens[0] == "Анфиса":
        return process_anfisa(tokens[1])
    else:
        return process_friend(tokens[0], tokens[1])


def process_friend(name, query):
    #print(query)
    if name in DATABASE:
        if query == "ты где?":
            return f"{name} в городе {DATABASE[name]}"
        else:
            return '<неизвестный запрос>'
    else:
        return f"У тебя нет друга по имени {name}"


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


runner()'''


'''import urllib.parse


url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'

# чтобы вычленить текст вопроса
# разбейте строку по знаку = и возьмите
# второй элемент получившегося списка
question =  url.split("=")# сохраните его в переменной question

# напечатайте на экран запрос в расшифрованном виде
print(urllib.parse.unquote(question[1])) # ваш код здесь'''

import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    'Accept-Language' : 'ru'
}

# не забудьте передать параметры и заголовки в http-запрос
# через аргументы `params` и `headers` функции get()
response = requests.get(url, params=weather_parameters, headers=request_headers)
print(response.text)

import random

print(random.randint(0, 1))