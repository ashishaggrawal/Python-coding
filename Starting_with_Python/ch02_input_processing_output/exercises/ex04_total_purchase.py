'''Ask for the price of five items, then display the subtotal,
the sales tax (7 percent) and the total.'''

TAX_RATE = 0.07

item1 = float(input('Price of item 1: $'))
item2 = float(input('Price of item 2: $'))
item3 = float(input('Price of item 3: $'))
item4 = float(input('Price of item 4: $'))
item5 = float(input('Price of item 5: $'))

subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * TAX_RATE
total = subtotal + tax

print()
print(f'{"Subtotal:":<12}${subtotal:>10,.2f}')
print(f'{"Sales tax:":<12}${tax:>10,.2f}')
print(f'{"Total:":<12}${total:>10,.2f}')
