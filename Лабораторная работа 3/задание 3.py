def count_letters(text):
    number_of_letters = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in number_of_letters:
                number_of_letters[letter] += 1
            else:
                number_of_letters[letter] = 1
    return number_of_letters


def calculate_frequency(number_of_letters):
    total_number_of_letters = sum(number_of_letters.values())
    frequency = {}
    for letter, count in number_of_letters.items():
        frequency[letter] = round(count / total_number_of_letters, 2)
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

frequency_of_writing_letters = calculate_frequency(count_letters(main_str))

for letter, frequency in frequency_of_writing_letters.items():
    print(f"{letter}: {frequency}")
