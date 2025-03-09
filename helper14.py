def days_to_units(num_of_days, conversion_unit):    
    
    if conversion_unit == "hours":
        return f"\n{num_of_days} days are {num_of_days * 24} hours" 
    elif conversion_unit == "minutes":
        return f"\n{num_of_days} days are {num_of_days * 24 * 60} minutes" 
    else:
        return "Unsupported unit. Please use 'hours' or 'minutes'."

def validate_and_execute(days_and_unit_dictionary):
    
    try:        
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number >0:
            calculate_value = days_to_units (user_input_number, days_and_unit_dictionary["unit"])
            print(calculate_value) 
        elif user_input_number == 0:
            print ("You entered zero. Please enter a positive integer greater than zero.")
        else:
            print ("Negative numbers are not allowed. Please enter a positive integer.")          
    except ValueError: 
        print("Invalid input! Please enter a valid positive integer for the number of days.")

user_input_message = "\nHey! Enter a number of days and conversion unit (e.g., '5-hours'). Type 'exit' to quit: "
