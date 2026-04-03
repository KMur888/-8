countries = {"Россия": "Москва", "Франция": "Париж", "Германия": "Берлин", "Италия": "Рим", "Япония": "Токио"}
print("Все страны и столицы:")
for country, capital in countries.items():
    print(country, "-", capital)
print("Столица Франции:", countries["Франция"])
sorted_countries = dict(sorted(countries.items()))
print("Отсортировано по странам:")
for country, capital in sorted_countries.items():
    print(country, "-", capital)