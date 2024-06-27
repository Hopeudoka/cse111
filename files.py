with open('courses.txt') as new_file:
    for line in new_file:
        parts = line.split(',')

        name = parts[0]
        grade = float(parts[1])
        line = line.strip()

        print(f'{name} - {grade}')



        