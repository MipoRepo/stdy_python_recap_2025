# Modules are logically organized code files
# --------------------------
#   import helper14      | Imports the whole module: you must use the module name when calling functions, e.g., helper_pr14.
#                           | You can rename the module using: import helper_pr14 as helper.
# --------------------------
#  from helper14 import *  | Imports all functions: you can use functions directly without prefixing them with the module name.
#                           | Note: This is generally not recommended, as it can cause naming conflicts.
# --------------------------


from helper14 import validate_and_execute, user_input_message 
# Best practice above       | Imports specific functions from the module, so you can use them directly without the module name.
#                           | This is a better practice than importing everything with '*' as it avoids naming conflicts.

user_input = ""
while user_input.lower() != "exit": 
    user_input = input(user_input_message)
    
    if user_input.lower() == "exit":
        break
    
    days_and_unit = user_input.split("-")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)

# Existing Python modules examples
# import math
# math.pow (2, 4)   = 2*2*2*2 = 16 
# math.sqrt (16)    = 4
# math.floor (5/2)  = 2
# 
# from datatime import datetime, timezone
#
import logging
# logger= logging.getLogger("Main")
# logger.error("Error happened")

#############################
# Tip: You can open the module file by holding 'Ctrl' and clicking on the module name.  
# This allows you to quickly navigate to the module's code.
# math -> opens math.pyi
# logging -> __init__.py

#############################