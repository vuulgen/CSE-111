import random
from re import X 


awesome_list = ['awesome', 'csel111', 'is', 'awesome']
print(awesome_list)

x = 10
print(x)

def some_function(num):
    num += 5
some_function(5)

print(x)
def pick_random_workd(list_of_words):
    list_of_words.append('superDuperAwesome')
    print(list_of_words)
    return random.choice(list_of_words)

pick_random_workd(awesome_list)
print(awesome_list)