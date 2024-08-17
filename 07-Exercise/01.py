'''Assuming no payments are made, how much would a $1,000 loan be worth at 5%
interest compounded monthly after 3 years?'''
def calclulate_compound_interest(amount,interest_rate,time):
    return amount*(1+(interest_rate/12))**(12*time)
print(calclulate_compound_interest(1000,0.05,3))