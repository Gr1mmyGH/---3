import re

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Знаходимо перше речення
            first_sentence = re.split(r'[.!?]', content)[0]
            print("Перше речення:", first_sentence)

            # Знаходимо всі слова та видаляємо пунктуацію
            words = re.findall(r'\b\w+\b', content)
            # Розділяємо слова на українські та англійські
            ukr_words = sorted([word for word in words if re.match(r'[а-яА-ЯіїєґІЇЄҐ]', word)], key=str.casefold)
            eng_words = sorted([word for word in words if re.match(r'[a-zA-Z]', word)], key=str.casefold)
            
            # Виводимо відсортовані слова та кількість
            print("Слова на українській:", ukr_words)
            print("Слова на англійській:", eng_words)
            print("Загальна кількість слів:", len(words))

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print("Сталася помилка:", str(e))

# Виклик функції
read_first_sentence("text.txt")  # замініть на назву вашого текстового файлу
