"""
#      Today we will Build a program 
#        Which will give us the area of a triangle
#        Formula: Square root of s(s - a)*(s - b)*(s - c)
#        # Here s is the "Semi_perimeter" = (sidea + sideb + sidec) / 2
"""
import math
def calc_area(sidea,sideb,sidec):
    semi_perimeter = (sidea + sideb + sidec) / 2
    area_of_triangle = semi_perimeter*(semi_perimeter - sidea)*(semi_perimeter - sideb)*(semi_perimeter - sidec)
    return math.sqrt(area_of_triangle)

side_a = int(input("Enter the dimenssion 1 : "))
side_b = int(input("Enter the dimenssion 2 : "))
side_c = int(input("Enter the dimenssion 3 : "))

area = calc_area(side_a,side_b,side_c)
print(area)

# print(f"{calc_area(side_a,side_b,side_c)} is the area of given triangle")
