# User input

user_input = input("He, enter a number of days and i will convert it to hours?\n")
print(user_input)

# Functions return value

cal_to_units = 24             
name_of_unit = "seconds"


def days_to_units(num_of_days):       
    return f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_unit}" # return f"value"
    
my_var = days_to_units(20)
print(my_var)

