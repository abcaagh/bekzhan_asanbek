def thesaurus(*args):
    staff_list = {}
    for i in range(len(args)):
        if not args[i][0] in staff_list:
            staff_list.setdefault(args[i][0], [args[i]])
        else:
            staff_list[args[i][0]].extend([args[i]])
    print(staff_list)


thesaurus("Иван", "Мария", "Петр", "Илья")
