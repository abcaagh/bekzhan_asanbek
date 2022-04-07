tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def turple_gen(tutors, klasses):
    len_args = len(klasses) - len(tutors)

    if len(tutors) > len(klasses):
        len_args = len(tutors) - len(klasses)
        for i in range(len(tutors) - len_args, len(tutors)):
            klasses.append('None')
    else:
        for i in range(len(klasses) - len_args, len(klasses)):
            tutors.append('None')

    for cell_1, cell_2 in zip(tutors, klasses):
        yield cell_1, cell_2


print(*turple_gen(tutors, klasses))
