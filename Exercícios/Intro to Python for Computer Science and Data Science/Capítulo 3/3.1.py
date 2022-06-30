# fig02_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0 # number of passes
failures = 0 # number of failures

# process 10 studentes
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1 = pass, 2 = fail): '))

    while result < 1 or result > 2:
        print('You input a invalid value.')
        result = int(input('Enter result (1 = pass, 2 = fail): '))

    if result == 1:
        passes = passes + 1
    elif result == 2:
        failures = failures + 1
    
# termination phase
print('Passed', passes)
print('Failed', failures)

if passes > 8:
    print('Bonus to instructor')