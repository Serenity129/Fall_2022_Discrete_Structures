import random
change_due = random.randint(50,1000)
print(f'Change due is {change_due}.')

working_total = change_due

##Dollars
dollars_due = working_total // 100
working_total = working_total % 100
if dollars_due > 0:
        print(f'You received: {dollars_due} dollars.')
elif dollars_due == 1:
        print(f'You received: 1 dollar.')

##Quarters
quarters_due = working_total // 25
working_total = working_total % 25
if quarters_due > 0:
        print(f'You received: {quarters_due} quarters.')
elif quarters_due == 1:
        print(f'You received: 1 quarter.')

##Dimes
dimes_due = working_total // 10
working_total = working_total % 10
if dimes_due > 0:
        print(f'You received: {dimes_due} dimes.')
elif dimes_due == 1:
        print(f'You received: 1 dime.')

##Nickles
nickels_due = working_total // 5
working_total = working_total % 5
if nickels_due > 0:
        print(f'You received: {nickels_due} nickels.')
elif nickels_due == 1:
        print(f'You received: 1 nickel.')

##Pennies
pennies_due = working_total // 1
working_total = working_total % 1
if pennies_due > 0:
        print(f'You received: {pennies_due} pennies.')
elif pennies_due == 1:
        print(f'You received: 1 penny.')

##Count Back Change
print(f'Total change is: {dollars_due} dollars, {quarters_due} quarters, {dimes_due} dimes, {nickels_due} nickels, and {pennies_due} pennies.')  

