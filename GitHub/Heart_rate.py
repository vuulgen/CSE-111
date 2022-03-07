"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
""" 
#def min_heart_rate():
 #   return int(220 - age * .65)
#def max_heart_rate():
 #   return int(220 - age * .85)

que = float(input('What is your age: '))

age = int(220 - que)
min = float(age * .65)
max = float(age * .85)

print(f'When you exercise to strengthen your heart, you should keep your heart rate between {min} and {max} beats per minute.')
a = 1
b = 3
c = -2
result = a + b * 7 % 4 - c
print(result)