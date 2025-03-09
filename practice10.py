# List data type 

my_list = ["January", "February", "March"]
print (my_list[2])
print(my_list)

my_list.append("April")
print(my_list)
print (len(my_list))

for list_item in my_list:
    print (list_item)
    
my_list.remove("January")
print(my_list)
print (len(my_list))