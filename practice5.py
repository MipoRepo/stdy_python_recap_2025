# Encapsulating 
# Cleaning code of practice4.py

cal_to_units = 24             
name_of_unit = "hours"


def days_to_units(num_of_days):    
    
    if num_of_days > 0:         
        return f"\n{num_of_days} days are {num_of_days * cal_to_units} {name_of_unit}" 
    elif num_of_days == 0:
        return "you enter zero, please enter a positive integer greater than zero. "


def validate_and_execute():
    
    if user_input.isdigit(): 
        
        user_input_number = int(user_input)

        calculate_value = days_to_units (user_input_number)
        print(calculate_value) 
        
    else:
        print("your input is not number, please enter a positive integer greater than zero. ")


user_input = input("Hey, enter a number of days and i will convert it to hours? ")
validate_and_execute()

