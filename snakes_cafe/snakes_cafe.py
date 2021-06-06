order_list = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado',
              'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears']

print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")

i = 0
while i >= 0:
    order = input("""
***********************************
** What would you like to order? **
***********************************
> """)
    i = i+1
    if (order.capitalize() in order_list):
        print(f'** {i} order of {order} have been added to your meal **')
    else:
        print(f'sorry {order} is not in the menu')
    if(order == 'quit'):
        break
