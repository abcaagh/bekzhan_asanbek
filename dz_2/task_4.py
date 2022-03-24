employee_info = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len((employee_info))):
    employee_info[i] = employee_info[i].split()[-1]
    print(f'Привет, {employee_info[i].title()}')

