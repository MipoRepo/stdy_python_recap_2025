# Basic data types

print("Hello World!") # String inside of double or single quotes
print(2.5) #Float
print(2) #Integer
print(-2) #Integer

# ------------------------------
# Strings

print("20 days are xx minutes")
print(20 * 24 * 60)

# ------------------------------
# String Concatenation, merkkijonojen ketjutus

print("20 days are " + str(50) + " minutes") # Old way

print(f"20 days are {50} minutes")           # New: f = formatting text or sting area, {} = non text, Python version after 3.X

print(f"20 days are {20 * 24 * 60} minutes") 

print(f"20 days are {20 * 24 * 60 * 60} seconds") 

# ------------------------------
# Variables

cal_to_sec = 20 * 24 * 60 * 60             # Variable naming convetion, syntax: Underline Or name with capitals "CalToSec"
name_of_unit = "seconds"

print(f"20 days are {20 * cal_to_sec} {name_of_unit}")
print(f"35 days are {35 * cal_to_sec} {name_of_unit}")
print(f"50 days are {50 * cal_to_sec} {name_of_unit}")
print(f"110 days are {110 * cal_to_sec} {name_of_unit}")

# ------------------------------
# Functions

cal_to_sec = 20 * 24 * 60 * 60             
name_of_unit = "seconds"


def days_to_units(num_of_days):       # name_of_function(input):
    print(f"{num_of_days} days are {num_of_days * cal_to_sec} {name_of_unit}")
    print("Good!")

#Calling function and giving value for function's variable
days_to_units(20)  
days_to_units(35)
days_to_units(50)
days_to_units(110) 

# -----
# Multiple function's variables
# Variable Scope's (laajuus): a) Global Scope:  [cal_to_sec] AND Local Scope, inside of function [num_of_days]

cal_to_sec = 20 * 24 * 60 * 60             
name_of_unit = "seconds"


def days_to_units2(num_of_days, message):       
    print(f"{num_of_days} days are {num_of_days * cal_to_sec} {name_of_unit}")
    print(message)


# Demo of scope's
def scope_check(num_of_days): 
    inside_var = "This variable only insede of funktion"
    print(name_of_unit) # Global variable
    print(num_of_days) # Local variable inside of scope_check funktion, not conected to days_to_units or days_to_units2 functions
    print(inside_var)
    
days_to_units2(20, "All good!")  
days_to_units2(35, "All good!")
days_to_units2(50, "All good!")
days_to_units2(110, "All good!")

scope_check(22)
