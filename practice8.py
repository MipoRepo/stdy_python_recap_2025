# While loop
# Is performed indefinitely or until the amount or other specified condition is met (boolean: until condition = false)

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


i = 0 
while i < 3:
    user_input = input("\nHey, enter a number of days and i will convert it to hours? ")
    validate_and_execute()
    i += 1
    print ("It was query number ", i)



user_input = ""
while user_input != "exit": # != means different than "exit"
    user_input = input("\nHey hey, enter a number of days and i will convert it to hours? (Or type exit to exit): ")
    if user_input.lower() != "exit": # word 'exit' do not need to validate - error message
       validate_and_execute()

# while True: | OPTION 2
#     user_input = input("\nHey, enter a number of days and i will convert it to hours? (Or type exit to exit): ")
#     if user_input.lower() == "exit":    # .lower - all in lowercase
#             break
#     validate_and_execute()
# 
# while True: | Option 3, indefinitely if not break, notice capital letter True
#     user_input = input("\nHey, enter a number of days and i will convert it to hours? (Or type exit to exit): ")
#     validate_and_execute()