# Dictionary data type
# Excample code conver to get input value of units from user 

def days_to_units(num_of_days, conversation_unit):    
    if conversation_unit == "hours":
        return f"\n{num_of_days} days are {num_of_days * 24} hours" 
    elif conversation_unit == "minutes":
        return f"\n{num_of_days} days are {num_of_days * 24 * 60} minutes" 
    else:
        return "unsupported unit"

def validate_and_execute():
    
    try:        
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number >0:
            calculate_value = days_to_units (user_input_number, days_and_unit_dictionary["unit"])
            print(calculate_value) 
        elif user_input_number == 0:
            print ("you entered zero, please enter a positive integer greater than zero. ")
        else:
            print ("you enter negative a number, please enter a positive integer greater than zero. ")          
    except ValueError: 
        print("your input is not a number, please enter a positive integer greater than zero. ")

user_input = ""
while user_input != "exit": 
    user_input = input("\nHey, enter a number of days and conversioin unit | days-unit.(type exit to exit): ")
    days_and_unit = user_input.split("-")
    print(days_and_unit)
    print(type(days_and_unit))
    if user_input.lower() != "exit":
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        print(days_and_unit_dictionary)
        print(type(days_and_unit_dictionary))
        validate_and_execute()