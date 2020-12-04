def findingAverage():    
    student_heights_input = input('Please type the heights separated by a comma: \nExample: 180, 124, 165, 173, 189, 169, 146\n')
    student_heights = student_heights_input.split(', ')
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])

    total_height = 0
    # Add the heights from the list together
    # Could have also used: total_height = sum(student_heights)
    for i in student_heights:
        total_height += i

    average_height = round(total_height / len(student_heights))
    print(f'The average height is {average_height}')

findingAverage()