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
ordered_item = []
i = 1
while i >= 1:
    order = input("""
***********************************
** What would you like to order? **
***********************************
> """)
    if order in ordered_item:
        i = i+1
    else:
        ordered_item.append(order)
        i = 1

    if (order.capitalize() in order_list):
        print(f'** {i} order of {order} have been added to your meal **')
    elif(order == 'quit'):
        break
    else:
        print(f'sorry {order} is not in the menu')
