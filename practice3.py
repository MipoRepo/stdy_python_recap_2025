# Functions return value 2

cal_to_units = 24             
name_of_unit = "hours"


def days_to_units(num_of_days):       
    return f"\n{num_of_days} days are {num_of_days * cal_to_units} {name_of_unit}" 
    

user_input = input("Hey, enter a number of days and i will convert it to hours? ")

calculate_value = days_to_units(int(user_input)) # Creating variable for printing of value
                                                 # Without "int" funcktion treats a variable as a string | Called: Casting

print(calculate_value)

# OR

user_input_number = int(user_input)
calculate_value2 = days_to_units (user_input_number)
print(calculate_value2) 