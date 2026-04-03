# Доп. задание на множества
# Создаем структуру данных: словарь, где ключ — имя студента, 
# а значение — множество (set) языков, которые он знает.

students_data = {
    "Алексей": {"Английский", "Испанский", "Китайский"},
    "Мария": {"Немецкий", "Английский"},
    "Иван": {"Французский", "Китайский", "Японский"},
    "Елена": {"Английский", "Французский"},
    "Дмитрий": {"Китайский", "Итальянский"}
}

# Определяем, сколько различных языков знают студенты
all_languages = set() # для всех языков

for languages in students_data.values():
    # Метод update добавляет элементы из другого множества, исключая дубликаты
    all_languages.update(languages)

print(f"Всего различных языков знают студенты: {len(all_languages)}")

# Выводим отсортированный список этих языков
sorted_languages = sorted(list(all_languages))
print(f"Список языков: {', '.join(sorted_languages)}")

# Выводим список студентов, которые знают китайский язык
target_language = "Китайский"
chinese_speakers = []

for student, languages in students_data.items():
    if target_language in languages:
        chinese_speakers.append(student)

print(f"Студенты, знающие {target_language}: {', '.join(chinese_speakers)}")