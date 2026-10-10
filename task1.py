students = [
    {"name": "Eli", "score": 85, "attendance": 80},
    {"name": "Veli", "score": 45, "attendance": 90},
    {"name": "Pirveli", "score": 60, "attendance": 60},
    {"name": "Turane", "score": 40, "attendance": 50},
    {"name": "Nurane", "score": 95, "attendance": 95},
    {"name": "Gulare", "score": 70, "attendance": 70}
]

passed_names = []
failed_names = {}

for student in students:
    name = student["name"]
    if student["score"] >= 51 and student["attendance"] >= 71 :
        passed_names.append(student["name"])
    else:
        if student["score"] < 51 and student["attendance"] < 71 :
            failed_names[name] = "both"
        elif student["score"] < 51 and student["attendance"] >=71 :
            failed_names[name] = "low score"
        else:
            failed_names[name] = "low attendance"

print("Keçen telebeler:", passed_names)
print("Kesilen telebeler ve sebebleri:", failed_names)