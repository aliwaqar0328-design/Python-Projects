""" This will fiter out
 the evens 
from the list """

list = [31,32,56,77,89,98,43,322,46,70,12,37,81]
filtered_list = [num for num in list if num % 2 == 0 ]
print(f"The filtered list is {filtered_list}")
print(len(filtered_list))