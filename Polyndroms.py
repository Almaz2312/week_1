words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил', 'language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
for word in words:
    lower_ = word.lower()
    reverse_ = (lower_[::-1])
    if reverse_ in lower_:
        print(word, "Полиндром")
    else:
        print(word, "Не полиндром")