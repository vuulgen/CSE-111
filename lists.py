# creating variables
student1 = 'Natalie'
student2 = 'Doubra'
student3 = 'Jase'
student4 = 'Lindsay'

# print(f"{student1} {student2} {student3} {student4}")

# creating a list
student_list = ['Natalie', 'Doubra', 'Jase', 'Lindsay']

# looping through a list
# for i in range(len(student_list)):
    # print(student_list[i])

# dictionaries vs lists
# create a dictionary
review = {
    'star_rating': 5,
    'username': 'freddy',
    'date': '02-14-22',
    'title': 'Best recipe ever',
    'description': 'Great recipe, the only thing that would make it better is cooking it at 350.',
    'images': ['amazon.com.img/22.png', 'amazon.com.img/23.png']
}

review2 = {
    'star_rating': 3,
    'username': 'jenny',
    'date': '02-12-22',
    'title': 'Most horrible recipe ever',
    'description': 'Great recipe, the only thing that would make it better is it actually being edible.',
    'images': ['amazon.com.img/55.png', 'amazon.com.img/253.png']
}


review_list = [review, review2]
# for i in range(len(review_list)):
#     print(review_list[i]['images'][1])

student = {
    'name': 'jenny johnson',
    'grade': 90.5
}
student2 = {
    'name': 'john johnson',
    'grade': 20
}

students = [student, student2]


colors = ['yellow', 'blue', 'red', 'green']
# loop with skips
for i in range(0, len(colors), 2):
    print(colors[i])

for i in(range(0, 101, 20)):
    print(i)

# adding to a list (how to append and insert)
student3 = {
    "name": "Sam Hopkins",
    "grade": 100
}
students.insert(0, student3)
# syntax: for i in list
# for i in students:
#     # if(i['grade'] < 70):
#     print(i['name'])

# removing from list
# slice lists
colors = ['yellow', 'blue', 'red', 'green', 'pink', 'purple', 'brown']
print(colors[3:6])
# joining two lists (item name and item price - dictionaries)
# filtering lists
# create list in function with default parameters
# create list in function with optional parameters

# Write a program that defines an empty list and then write 3 functions, one to add on to the end of the list, one to add an item somewhere not at the beginning or the end of the list, and one that removes an item from the list. 
# Both of the functions that add data should take in a parameter received by the user to be added to the list
# Create a loop that will call each of these 3 functions 5 times and then print the list when the loop has finished.
