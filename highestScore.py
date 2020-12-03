student_scores_input = input('Input a list of student scores: ')
student_scores = student_scores_input.split(' ')

# Take the input and convert from str to int
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Iterate though the list items to find the highest value
# Could use: max(student_scores)
high_score = student_scores[0]
for i in range(len(student_scores)):
    if student_scores[i] > high_score:
        high_score = student_scores[i]

print(f'The highest score in the class is: {high_score}')