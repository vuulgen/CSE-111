def get_num_in_range(prompt, min, max):
    while True:
        try:
            number = float(input(prompt))
            if min <= number <= max:
                return number
            else:
                print("Please enter a number between 0 and 100 percent. :)")
        except:
            print("Please enter a valid number.")