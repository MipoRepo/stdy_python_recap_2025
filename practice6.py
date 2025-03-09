# Nested loops statements | if..else  (sisäkkäiset silmukat)

cal_to_units = 24             
name_of_unit = "hours"


def days_to_units(num_of_days):    
             
    return f"\n{num_of_days} days are {num_of_days * cal_to_units} {name_of_unit}" 
    

def validate_and_execute():
    
    if user_input.isdigit(): 
        
        user_input_number = int(user_input)

        if user_input_number >0:
            calculate_value = days_to_units (user_input_number)
            print(calculate_value) 
        elif user_input_number == 0:
            print ("you enter zero, please enter a positive integer greater than zero. ")
    
    else:
        print("your input is not number, please enter a positive integer greater than zero. ")


user_input = input("Hey, enter a number of days and i will convert it to hours? ")
validate_and_execute()

# Note: nested loops are not always the clearest way to create code.