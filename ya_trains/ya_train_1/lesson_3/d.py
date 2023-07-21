def count_unique_words(text):
    words = text.split()
    unique = set()
    for word in words:
        #word = word.strip('.,!?;:"')
        unique.add(word)
    return len(unique)


if __name__ == "__main__":
    # Вместо чтения из sys.stdin, присваиваем значение текста для тестирования
    input_text = """She sells sea shells on the sea shore;
    The shells that she sells are sea shells I'm sure.
    So if she sells sea shells on the sea shore,
    I'm sure that the shells are sea shore shells."""

    # Получаем количество различных слов
    result = count_unique_words(input_text)

    # Выводим результат
    print(result)
