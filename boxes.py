import math

item_number = float(input('Enter the number of items: '))
item_per_box = float(input('Enter the number of items per box: '))
time_rate = float(input('How long are you willing to wait for shipping'
 '(IE: (1)overnight shipping is 26.35 per box, (2)one day shipping is 23.71, (3)two day shipping '
 '21.33 (4)anything else varies.) '))
if time_rate == 1:
    price_per_box = 26.35
elif time_rate == 2:
    price_per_box = 23.71
elif time_rate == 3:
    price_per_box = 21.33
else:
    price_per_box = 21.33 / .10 

box_number = math.ceil(item_number / item_per_box)
total_price = box_number * price_per_box

print(f'For {item_number} items, packing {item_per_box} items in each box, you will need {box_number} boxes.'
f'This will total out at {total_price:.2f} ')