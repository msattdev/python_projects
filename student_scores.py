student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 90, 100, 110, 120, 130, 140, 150]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)