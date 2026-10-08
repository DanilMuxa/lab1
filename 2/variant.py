total = int(input('Введите кол-во участников: '))
team = int(input('Введите кол-во участников в команде: '))

full = total // team
left = total % team
team_count = (total + team - 1) // team

print(f'''Полных команд: {full}
Осталось участников: {left}
Минимум команд: {team_count}''')
