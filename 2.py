# create a dictionary named student_scores where keys are student name and values are their scores (integers).
student_scores = {
    "Anne": 45,
    "Baanu": 34,
    "Rudsi": 99,
    "Lala": 67,
    "Tintu": 95
}

print("---Initial Student scores---")

# Iterate through the dictionary and print each student's name and their scores

for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\n")

# Add a new student and their score to the dictionary

new_student_name = "Rasi"
new_student_score = 100
student_scores[new_student_name] = new_student_score
print(f"---Added New Student: {new_student_name}: {new_student_score}")
for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\n")