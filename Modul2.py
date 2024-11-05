from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def TransLate(text: str, scr: str, dest: str) -> str:
    """Перекладає текст на задану мову або повертає повідомлення про помилку."""
    try:
        translation = GoogleTranslator(source=scr, target=dest).translate(text)
        return translation
    except Exception as e:
        return f"Помилка: {str(e)}"

def LangDetect(text: str, set_option: str = "all") -> str:
    """Визначає мову та коефіцієнт довіри або повертає повідомлення про помилку."""
    try:
        language = detect(text)
        # `langdetect` не дає коефіцієнт довіри, тому повертається тільки мова.
        return language if set_option in ["lang", "all"] else "Коефіцієнт довіри недоступний"
    except Exception as e:
        return f"Помилка: {str(e)}"
