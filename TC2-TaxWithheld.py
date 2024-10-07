# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Get user input 
    salary = float(input("Please enter the full amount of your weekly salary:"))
    dependents = int(input("Please enter how many dependents ou have:"))

    #Define tax calculations 
    provincial_tax_withheld = 60.00
    federal_tax = 250.00
    dependent_deduction_per_depedent = 40.00 

    #Calculate dependent deduction 
    dependent_deduction = dependent_deduction_per_depedent * dependents 

    #Calculate total tax withheld 
    total_tax_withhold = provincial_tax_withheld + federal_tax - dependent_deduction_per_depedent 

    #Calculate the take home pay 
    take_home_pay = salary - federal_tax 
    
    #Output the results 
    print(f"\nProvincial tax withheld: ${provincial_tax_withheld:.2f}") 
    print(f"\nfederal tax withheld: ${federal_tax:.2f}")
    print(f"\nDependent deduction for {dependents}dependents: ${dependent_deduction:.2f}")
    print(f"Total tax withheld: ${total_tax_withhold:.2f}")
    print(f"Total take-home pay: ${take_home_pay:.2f}")
    # YOUR CODE ENDS HERE

main()
