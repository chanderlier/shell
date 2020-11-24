names = ['refrain', 'dieser', 'kate', 'jessie', 'angela']
courses = ['Chinese', 'Math', 'English']
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)
