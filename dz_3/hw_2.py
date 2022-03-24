def thesaurus(*args):
    employee_name = {}
    for i in args:
        key_name = i[0]
        if key_name in employee_name:
            employee_name[key_name].append(i)
        else:
            employee_name[key_name] = [i]
    print(employee_name)


thesaurus("Иван", "Мария", "Петр", "Илья", "Петруша")
