name_a = input('Название первого предмета: ')
count_a = int(input(f'Сколько занятий в неделю: '))
length_a = int(input(f'Длительность одного занятия в минутах: '))
name_b = input('Название второго предмета: ')
count_b = int(input(f'Сколько занятий в неделю: '))
length_b = int(input(f'Длительность одного занятия в минутах: '))
week_limit = float(input('Сколько часов в неделю доступно всего: '))


minutes_a = count_a * length_a          
minutes_b = count_b * length_b          

week_minutes = minutes_a + minutes_b    
week_hours = week_minutes / 60          

free_hours = week_limit - week_hours   
month_hours = week_hours * 4            


print('-----------------------------------')
print('АНАЛИЗ УЧЕБНОЙ НАГРУЗКИ')
print(f'Предмет {name_a}: {minutes_a} мин в неделю')
print(f'Предмет {name_b}: {minutes_b} мин в неделю')
print(f'Всего за неделю: {week_minutes} мин ({week_hours:.2f} ч)')
print(f'Свободное время: {free_hours:.2f} ч')
print(f'Нагрузка за 4 недели: {month_hours:.2f} ч')
print('-----------------------------------')
