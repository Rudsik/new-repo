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


# Find the student with a higher score and print their name and score
if student_scores:
    highest_score = 0
    highest_scorer_name = ""
    for name, score in student_scores.items():
        if score > highest_score:
            highest_score = score
            highest_scorer_name = name
    print(f"---Student with a Higher Score---")
    print(f"{highest_scorer_name}: {highest_score}\n")
else:
    print("The dictionary is empty, cannot find the highest score.\n")