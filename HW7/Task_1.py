# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке.

# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод: Парам пам-пам

poem = input("Enter a poem -> ")

list_of_phrases = poem.split()
counter = list_of_phrases[0].count('а')
for phrase in list_of_phrases:
    if phrase.count('а') == counter:
        pass
    else:
        print('Пам парам')
        break
else:
    print('Парам пам-пам')


