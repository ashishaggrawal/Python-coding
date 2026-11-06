'''A company's profit is usually about 23 percent of its total sales.
Ask the user for the projected total sales and display the expected profit.'''

PROFIT_RATE = 0.23

total_sales = float(input('Enter the projected total sales: $'))

profit = total_sales * PROFIT_RATE

print(f'Expected profit: ${profit:,.2f}')
