#  Simple quest 1 - Create a loan calculator
#  * Have the user enter the cost of the loan, the interest rate, and the number of years of the loan
#  * Calculate monthly payments with the following formula
#  M = L [ i ( 1 + i ) n ] / [ ( 1 + i ) n-1 ]
#  ** M = monthly payment
#  ** L = loan amount
#  ** i = interest rate (for an interest rate of 5%, i = 0.05)
#  ** n = number of payments

#How much the user want to loan - converting str to float
loanAmount = float(input("Please enter your loan amount: "))
#How much is the interesting hate - converting str to float
interestRate = float(input("Please enter your interest rate: "))
#Number of payments - converting str to float
numberOfPayments = float(input("Please enter the number of payments: "))
#calculating the monthly payment
monthlyPayment = float((loanAmount * (interestRate * (interestRate + 1) * numberOfPayments)) / (
            (interestRate + 1) * (numberOfPayments - 1)))
#Displaying the results using .format function
print('Payment will be {0:d} times of {1:.2f}'.format(int(numberOfPayments), monthlyPayment))
