"""
 Celcius to Fahrenheit
"""
def celcius_to_fahrenheit(x):
    fahrenheit = (x * 9//5) + 32
    return fahrenheit

value =int(input("Enter your Celcius temparature : "))
converted_temprature =celcius_to_fahrenheit(value)
print("Your Temprature in Fahrenheit is", converted_temprature)