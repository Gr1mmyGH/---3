import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Функція для обчислення віку
def calculate_age(birth_date):
    return datetime.now().year - birth_date.year

# Ініціалізація змінних
male_count, female_count = 0, 0
age_categories = {"<18": 0, "18-45": 0, "45-70": 0, ">70": 0}
gender_age_categories = {"<18": {"Чоловік": 0, "Жінка": 0}, "18-45": {"Чоловік": 0, "Жінка": 0}, "45-70": {"Чоловік": 0, "Жінка": 0}, ">70": {"Чоловік": 0, "Жінка": 0}}

try:
    # Спроба відкрити файл CSV
    with open("employees.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Пропустити заголовок

        # Обробка рядків CSV
        for row in reader:
            try:
                gender = row[3].strip()
                birth_date = datetime.strptime(row[4], "%Y-%m-%d")
                age = calculate_age(birth_date)

                # Підрахунок статей
                if gender == "Чоловік":
                    male_count += 1
                elif gender == "Жінка":
                    female_count += 1
                else:
                    print(f"Невідома стать у рядку: {row}")
                    continue

                # Визначення вікової категорії
                if age < 18:
                    age_category = "<18"
                elif 18 <= age <= 45:
                    age_category = "18-45"
                elif 45 < age <= 70:
                    age_category = "45-70"
                else:
                    age_category = ">70"

                # Підрахунок за віковими категоріями
                age_categories[age_category] += 1
                gender_age_categories[age_category][gender] += 1

            except ValueError as ve:
                print(f"Помилка у рядку {row}: {ve}")
            except IndexError:
                print(f"Недостатньо даних у рядку: {row}")

    # Вивід результатів
    print("Кількість чоловіків:", male_count)
    print("Кількість жінок:", female_count)
    print("Кількість у вікових категоріях:", age_categories)
    print("Кількість за статтю у вікових категоріях:", gender_age_categories)

    # Побудова діаграм
    # Діаграма за статтю
    plt.figure(figsize=(10, 6))
    plt.bar(["Чоловіки", "Жінки"], [male_count, female_count], color=['blue', 'pink'])
    plt.title("Розподіл за статтю")
    plt.show()

    # Діаграма за віковими категоріями
    plt.figure(figsize=(10, 6))
    plt.bar(age_categories.keys(), age_categories.values(), color='orange')
    plt.title("Розподіл за віковими категоріями")
    plt.show()

    # Діаграми за статтю у вікових категоріях
    for category, counts in gender_age_categories.items():
        plt.figure(figsize=(10, 6))
        plt.bar(counts.keys(), counts.values(), color=['blue', 'pink'])
        plt.title(f"Розподіл за статтю у віковій категорії {category}")
        plt.show()

except FileNotFoundError:
    print("Помилка: Файл employees.csv не знайдено.")
except Exception as e:
    print("Непередбачена помилка:", e)
