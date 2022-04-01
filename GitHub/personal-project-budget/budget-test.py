lines_to_add = input('Enter lines to add to budget.txt: ')
with open("budget-test.txt", "a+") as f:
    f.writelines(lines_to_add)