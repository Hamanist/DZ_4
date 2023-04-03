words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {}
count = 0

words = words_easy, words_medium, words_hard

print('Выберите уровень сложности.\nЛегкий, Средний, Сложный.')
user = input('-> ').lower()
if user == 'легкий':
    words = words_easy
elif user == 'средний':
    words = words_medium
elif user == 'сложный':
    words = words_hard
else:
    print('Нет такого уровня')

user = input('Выбран уровень сложности, мы предложим 5 слов, подберите перевод.\nНажмите Enter.')

for key, value in words.items():
    print(f'{key}, {len(value)} букв, начинается на {value[0]}...\n')
    user = input('Ваш ответ - ').lower()
    if user in value:
        print(f'Верно, {key} — это {value}.\n')
        count += 1
        answers[key] = True
    else:
        print(f'Неверно. {key} — это {value}.\n')
        answers[key] = False

print('Правильно отвечены слова:')
for question in answers:
    if answers[question]:
        print(f'{question}')
print(f'\nНеправильно отвечены слова:')
for question in answers:
    if not answers[question]:
        print(f'{question}')

print(f'\nВаш ранг:\n{levels[count]}')
