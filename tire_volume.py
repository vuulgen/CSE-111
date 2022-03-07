import math
from datetime import datetime, timedelta
current_date_and_time = datetime.now()

width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume_p1 = math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + (2540 * diameter)) / 10000000000
# volume_p2_liters = volume_p1 / 10000000000

print(f'The approximate volume is {volume_p1:.2f} liters')

with open('volumes.txt', 'at') as volumestxt:
    volumestxt.write(f'Width: {width}. Aspect Ratio: {aspect_ratio}. Diameter: {diameter}. \n')
    volumestxt.write(f'The approximate volume is {volume_p1:.2f} liters\n')
    volumestxt.write(f"{current_date_and_time}\n")
    print('\n')

