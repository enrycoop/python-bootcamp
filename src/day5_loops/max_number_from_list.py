student_scores = "78 65 89 86 55 91 64 89".split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_score = student_scores[0]
for n in range(1, len(student_scores)):
    if student_scores[n] > max_score:
        max_score = student_scores[n]
print(f"The highest score in the class is: {max_score}")