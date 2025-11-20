                                            ### RENT CALCULATOR ###
               # Inputs we need from the user
# Total Rent
# Total food order for snacking
# Electricity units spended
# Charge per unit
# Number of  person living in the room

                # OUTPUT

    # Total amount you have to pay 

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

Rent = int(input("Enter your hostel/flat total rent : "))
Food = int(input('Enter the cost of food ordered : '))
Electricity_Units = int(input("Enter the amount of electricity units consumed : "))
Charge_per_unit = int(input("enter the charge per unit : "))
Persons_living = int(input("Enter the amount of persons living in the room : "))

total_electricity_bill = Electricity_Units * Charge_per_unit
Total_Bill_Person_wise = (total_electricity_bill + Rent + Food ) //  Persons_living
print("Your Rent is ", Total_Bill_Person_wise)


