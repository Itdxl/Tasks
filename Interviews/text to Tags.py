# Take a text and count every unique world.

str  = 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for  will uncover many web sites still in their infancy.'

def remove_marks(str):
    new_text = str.replace(',', ' ').replace('.', ' ')
    return new_text

# result = remove_marks(str)
# print(result)

# method maketrans() to delete all charachters, it does on on one mapping of symbols to delete

def remove_through_translate(text):
    # Создаем таблицу перевода, где запятые и точки будут заменены на None (удаляются)
    # Первый аргумент это строка, которую хотим перевести, в нашем случае пустой
    # Второй аргумент говорит, какие символы мы хотим заменить на аргументы из третьего.
    # Но если второй аргумент это пустая стока, то из текста будут удалены символы из 3 строки.
    translation_table = text.maketrans('', '', ',.')
    # Применяем таблицу перевода к тексту
    cleaned_text = text.translate(translation_table)
    return cleaned_text

def text_to_dict_unique(cleaned_text):
    dictionary = {}
    splitted = cleaned_text.split(' ')
    for word in splitted:
        if word in dictionary:
            dictionary[word] += 1
        dictionary[word] = 1
    return dictionary

remove = remove_through_translate(str)
result = text_to_dict_unique(remove)
print(result)