import os
import re
from Modul1 import TransLate, LangDetect

# Конфігураційний файл з параметрами
config = {
    "input_file": "input.txt",           # Назва файлу з текстом
    "target_language": "en",              # Мова, на яку потрібно перекласти
    "output": "screen",                   # Вивід: "screen" або "file"
    "max_chars": 600,                     # Максимальна кількість символів
    "max_words": 100,                     # Максимальна кількість слів
    "max_sentences": 15                    # Максимальна кількість речень
}

def count_words(text):
    return len(text.split())

def count_sentences(text):
    import re
    return len(re.findall(r'[.!?]', text))

# Основний код для зчитування, перевірки та перекладу тексту
if os.path.exists(config["input_file"]):
    with open(config["input_file"], "r", encoding="utf-8") as file:
        text = file.read()
    
    # Перевірка обмежень для символів, слів та речень
    if len(text) > config["max_chars"]:
        text = text[:config["max_chars"]]
    if count_words(text) > config["max_words"]:
        words = text.split()[:config["max_words"]]
        text = ' '.join(words)
    if count_sentences(text) > config["max_sentences"]:
        sentences = re.split(r'(?<=[.!?])', text)[:config["max_sentences"]]
        text = ''.join(sentences)
    
    # Переклад тексту
    translation = TransLate(text, "auto", config["target_language"])
    
    # Вивід перекладу на екран або у файл
    if config["output"] == "screen":
        print("Переклад на", config["target_language"] + ":")
        print(translation)
    else:
        output_file = f"{config['input_file'].split('.')[0]}_{config['target_language']}.txt"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(translation)
        print("Ok - Переклад збережено у файл", output_file)
else:
    print("Файл не знайдено")
