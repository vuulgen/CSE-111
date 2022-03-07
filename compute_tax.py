from tools import input_float

def prompt_for_income():
    income = input_float("Please enter your annual income: ")
    return income

def compute_tax(amount):
    tax = amount * .06
    return tax

def main():
    print(compute_tax(prompt_for_income()))

main()