students = [
    {"name": "Eli", "score": 85, "attendance": 80},
    {"name": "Veli", "score": 45, "attendance": 90},
    {"name": "Pirveli", "score": 60, "attendance": 60},
    {"name": "Turane", "score": 40, "attendance": 50},
    {"name": "Nurane", "score": 95, "attendance": 95},
    {"name": "Gulare", "score": 70, "attendance": 70}
]

def all_match(items, predicate):
    for item in items:
        if not predicate(item):
            return False
    return True

def any_match(items, predicate):
    for item in items:
        if predicate(item):
            return True
    return False

def attendance_minimum_50(student) :
    return student["attendance"] >= 50 

result_all_named = all_match(students, attendance_minimum_50)
print("Hərkəsin davamiyyəti minimum 50%-dir?", result_all_named)

result_all_lambda = all_match(students, lambda s: s["score"] > 50)
print("Hərkəsin balı 50-dən yuxarıdır?", result_all_lambda)

def score_90_plus(student) :
    return student["score"] >= 90

result_any_named = any_match(students, score_90_plus)
print("90 və ya daha çox balı olan var?", result_any_named)

result_any_lambda = any_match(students, lambda s: s["attendance"] == 100)
print("Davamiyyəti 100% olan var?", result_any_lambda)