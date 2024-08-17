'''Assuming no payments are made, how much would a $1,000 loan be worth at 5%
interest compounded continuously after 3 years?'''
from math import exp
def calculate_continuous_interest(amount,interest_rate,time):
    return amount*exp(time*interest_rate)
print(calculate_continuous_interest(1000,.05,3))