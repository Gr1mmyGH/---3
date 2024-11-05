from Modul1 import TransLate, LangDetect, LanguageList

print("Переклад:", TransLate("Як ти?", "auto", "en"))
print("Визначення мови:", LangDetect("Привіт"))
print(LanguageList("screen", "Добрий день"))