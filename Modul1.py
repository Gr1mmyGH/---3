from googletrans import Translator

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    """Перекладає текст на задану мову або повертає повідомлення про помилку."""
    try:
        translation = translator.translate(text, src=scr, dest=dest)
        return translation.text
    except Exception as e:
        return f"Помилка: {str(e)}"

def LangDetect(text: str, set_option: str = "all") -> str:
    """Визначає мову та коефіцієнт довіри або повертає повідомлення про помилку."""
    try:
        detection = translator.detect(text)
        if set_option == "lang":
            return detection.lang
        elif set_option == "confidence":
            return detection.confidence
        return f"Мова: {detection.lang}, Впевненість: {detection.confidence}"
    except Exception as e:
        return f"Помилка: {str(e)}"

def CodeLang(lang: str) -> str:
    """Повертає код мови або назву мови, залежно від параметру."""
    from googletrans.constants import LANGUAGES, LANGCODES
    lang = lang.lower()
    if lang in LANGCODES:
        return lang
    elif lang in LANGUAGES:
        return LANGUAGES[lang]
    else:
        return "Помилка: Невідома мова"

def LanguageList(out: str = "screen", text: str = "") -> str:
    """Виводить таблицю мов і перекладеного тексту на екран або у файл."""
    from googletrans.constants import LANGUAGES
    table = "N\tLanguage\tISO-639 code\tText\n"
    table += "-" * 50 + "\n"
    for i, (code, language) in enumerate(LANGUAGES.items(), 1):
        translated_text = TransLate(text, "auto", code) if text else ""
        table += f"{i}\t{language.capitalize()}\t{code}\t{translated_text}\n"
    if out == "file":
        with open("languages.txt", "w") as file:
            file.write(table)
    else:
        print(table)
    return "Ok"