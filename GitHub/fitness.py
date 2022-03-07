# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender(M/F): ").capitalize()
    birth_str = (input("Please enter your birhtdate(YYYY-MM-DD): "))
    pounds = float(input("Please enter your weight in U.S. pounds: "))
    inches = float(input("Please enter your height in U.S. inches: "))
    
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    weight_in_kilograms = kg_from_lb(pounds)
    years = compute_age(birth_str)
    height = cm_from_in(inches)
    bmi = body_mass_index(weight_in_kilograms, height)
    bmr = basal_metabolic_rate(gender, weight_in_kilograms, height, years)
    # Print the results for the user to see.
    print(f'pounds: {pounds:.2f} Kilagrams:{weight_in_kilograms:.2f}')
    print(f'Age: {years}')
    print(f'Inches: {inches:.1f} Centemeters: {height:.1f}')
    print(f'BMI: {bmi:.1f}')
    print(f'BMR: {bmr:.0f}')

    return


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight_in_kilograms = pounds * 0.45359237
    return weight_in_kilograms


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height = inches * 2.54
    return height


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = 10000 * weight / height ** 2
    return bmi


def basal_metabolic_rate(gender, weight_in_kilograms, height, years):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == 'F':
        bmr = 447.593 + 9.247 * weight_in_kilograms + 3.098 * height - 4.330 * years

    elif gender == 'M': 
        bmr = 88.362 + 13.397 * weight_in_kilograms + 4.799 * height - 5.677 * years

    return bmr

# Call the main function so that
# this program will start executing.
main()


# print(f'Age (years): {compute_age}')
# print(f'Weight (kg): {kg_from_lb}')
# print(f'Height (cm): {cm_from_in}')
# print(f'Body mass index: {body_mass_index}')
# print(f'Basal metabolic rate (kcal/day): {basal_metabolic_rate}')

