# Error handling
# Try / Except

cal_to_units = 24             
name_of_unit = "hours"


def days_to_units(num_of_days):    
             
    return f"\n{num_of_days} days are {num_of_days * cal_to_units} {name_of_unit}" 
    

def validate_and_execute():
    
    try:
        
        user_input_number = int(user_input)

        if user_input_number >0:
            calculate_value = days_to_units (user_input_number)
            print(calculate_value) 
        elif user_input_number == 0:
            print ("you enter zero, please enter a positive integer greater than zero. ")
        else:
            print ("you enter negative number, please enter a positive integer greater than zero. ")
            
    except ValueError:  # negative number is not error
        print("your input is not number, please enter a positive integer greater than zero. ")


user_input = input("Hey, enter a number of days and i will convert it to hours? ")
validate_and_execute()
