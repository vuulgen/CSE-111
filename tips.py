from click import prompt
from tools import get_num_in_range

# import from another folder on computer:
# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

def compute_tip(total, percentage):
    return total * percentage / 100

def prompt_percentage():
    percentage = get_num_in_range("what percentage would you like to tip? ", 0, 100)
    return percentage


print(prompt_percentage())