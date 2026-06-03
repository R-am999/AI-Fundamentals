# Student Grade Calculator
'''
marks = int(input())
if marks >= 90:
    print('A Grade')
elif marks >= 75 and marks <= 89:
    print('B Grade')
elif marks >= 60 and marks <= 74:
    print('C Grade')
elif marks >= 40 and marks <= 59:
    print('D Grade')
else:
    print('Fail')
'''

# Online Shopping Discount
'''
amount = int(input('Enter amount: '))
is_premium = input('A premium user? y/n: ')
payable_amount = amount

if amount >= 10000:
    payable_amount -= (20/100)*amount
elif amount >= 5000 and amount < 10000:
    payable_amount -= (10/100)*amount
elif amount >= 2000 and amount < 5000:
    payable_amount -= (5/100)*amount
else:
    pass

if is_premium == 'y':
    payable_amount -= (5/100)*amount

print("Amount:", int(payable_amount))
'''

# Employee Salary Processing
'''
salaries = [100000, 500000, 300000, 200000, 400000]
total_salary_payout = [(salary-(5/100)*salary) for salary in salaries]

max_sal = salaries[0]
for salary in salaries:
    if salary > max_sal:
        max_sal = salary

total = 0
for salary in salaries:
    total += salary
avg_sal = total/len(salaries)

print("In hand pay:", total_salary_payout)
print("Highest Salary:", max_sal)
print("Average Salary:", avg_sal)
'''

# Student Result Management
'''
maths=85
science=0
english=0
social=100
computer=88

def calc_marks(maths, science, english, social, computer):
    return maths+science+english+social+computer
total = calc_marks(maths, science, english, social, computer)

def calc_avg():
    return calc_marks(maths, science, english, social, computer)/5

def grade():
    if total >= 450:
        return 'A Grade'
    elif total >= 400:
        return 'B Grade'
    elif total >= 350:
        return 'C Grade'
    elif total >= 300:
        return 'D Grade'
    else:
        return 'E Grade'

def remarks():
    if total >= 300:
        return 'Pass'
    return 'Fail'

print(total)
print(calc_avg())
print(grade())
print(remarks())
'''
