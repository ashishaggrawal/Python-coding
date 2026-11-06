'''A car travels at 70 miles per hour. Show how far it goes in
6 hours, 10 hours and 15 hours.  (distance = speed * time)'''

SPEED = 70  # miles per hour

distance_6 = SPEED * 6
distance_10 = SPEED * 10
distance_15 = SPEED * 15

print(f'{"Hours":<8}{"Distance (miles)":>18}')
print(f'{6:<8}{distance_6:>18,}')
print(f'{10:<8}{distance_10:>18,}')
print(f'{15:<8}{distance_15:>18,}')
