import functools

students = [
    {"name": "Eli", "score": 85, "attendance": 80},
    {"name": "Veli", "score": 45, "attendance": 90},
    {"name": "Pirveli", "score": 60, "attendance": 60},
    {"name": "Turane", "score": 40, "attendance": 50},
    {"name": "Nurane", "score": 95, "attendance": 95},
    {"name": "Gulare", "score": 70, "attendance": 70}
]

passed_students = list(filter(lambda s: s["score"] >= 51 and s["attendance"] >= 71, students))

passed_names = list(map(lambda s: s["name"], passed_students))

passed_names_sorted = sorted(passed_students, key=lambda s: s["score"], reverse=True)

if passed_students :
    average_score = functools.reduce(lambda x, s: x + s["score"], passed_students, 0) / len(passed_students)
else :
    average_score = 0

print("Keçen telebeler: ", passed_names)
print("Ballarına görə sıralanmış keçən tələbələr: ", passed_names_sorted)
print("Keçənlərin orta balı: ", average_score)