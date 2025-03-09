# Set data type 

cal_to_units = 24             
name_of_unit = "hours"


def days_to_units(num_of_days):    
             
    return f"\n{num_of_days} days are {num_of_days * cal_to_units} {name_of_unit}" 
    

def validate_and_execute():
    
    try:        
        user_input_number = int(num_of_days_element)
        if user_input_number >0:
            calculate_value = days_to_units (user_input_number)
            print(calculate_value) 
        elif user_input_number == 0:
            print ("you entered zero, please enter a positive integer greater than zero. ", num_of_days_element)
        else:
            print ("you enter negative a number, please enter a positive integer greater than zero. ", num_of_days_element)          
    except ValueError:  # negative number is not error
        print("your input is not a number, please enter a positive integer greater than zero. ", num_of_days_element)

user_input = ""
while user_input != "exit": 
    user_input = input("\nHey hey, enter a number of days and i will convert it to hours? (Or type exit to exit): ")
    if user_input.lower() != "exit":
        for num_of_days_element in set (user_input.split(",")): 
            num_of_days_element = num_of_days_element.strip() 
            validate_and_execute()
            
            # If same input entered multiple times, 
            # validate_and_execute funktion is called only once. 
            # Set does NOT allow duplicate values