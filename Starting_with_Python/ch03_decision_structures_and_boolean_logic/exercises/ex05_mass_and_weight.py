'''Ask for an object's mass in kilograms and work out its weight in
newtons (weight = mass x 9.8). Say if the object is too heavy
(over 500 N) or too light (under 100 N).'''

GRAVITY = 9.8
MAX_WEIGHT = 500
MIN_WEIGHT = 100

mass = float(input("Enter the object's mass in kg: "))

weight = mass * GRAVITY

print(f'Weight: {weight:,.2f} newtons')

if weight > MAX_WEIGHT:
    print('The object is too heavy.')
elif weight < MIN_WEIGHT:
    print('The object is too light.')
