import csv
from faker import Faker
import random
from datetime import datetime

fake = Faker(locale='uk_UA')

# Словники з чоловічими та жіночими по батькові
male_patronymics = ["Іванович", "Петрович", "Сергійович", "Олександрович", "Миколайович", "Володимирович", "Богданович", "Григорович", "Дмитрович", "Романович", "Тимофійович", "Юрійович", "Олегович", "Васильович", "Георгійович", "Ігорович", "Максимович", "Андрійович", "Павлович", "Федорович"]
female_patronymics = ["Іванівна", "Петрівна", "Сергіївна", "Олександрівна", "Миколаївна", "Володимирівна", "Богданівна", "Григорівна", "Дмитрівна", "Романівна", "Тимофіївна", "Юріївна", "Олегівна", "Василівна", "Георгіївна", "Ігорівна", "Максимівна", "Андріївна", "Павлівна", "Федорівна"]

# Функція для генерації записів
def generate_employee_data():
    gender = random.choices(["M", "F"], [0.6, 0.4])[0]
    last_name = fake.last_name_male() if gender == "M" else fake.last_name_female()
    first_name = fake.first_name_male() if gender == "M" else fake.first_name_female()
    patronymic = random.choice(male_patronymics) if gender == "M" else random.choice(female_patronymics)
    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()
    return [last_name, first_name, patronymic, "Чоловік" if gender == "M" else "Жінка", birth_date, position, city, address, phone, email]

# Генерація CSV файлу з даними
with open("employees.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження", "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"])
    for _ in range(2000):
        writer.writerow(generate_employee_data())
