import random

# Monte Carlo simulation of the birthday paradox.
    
def generate_first_set_of_birthdays():
# create_random_birthdays()
# 
# Objective: 
#            Creates a list of randomly generated birthdays of n length. n is a
#            number entered by the user.
# Inputs:
#            None
#
# Outputs:
#            date_strings - list of randomly generated birthdays as strings
#

    print('Hello!\n')
    while True:
        num_birthdays = input('How many birthdays would you like me to generate?\n')
        try:
            num_birthdays = int(num_birthdays)
            if num_birthdays > 0:
                break
            else:
                print('Input must be a positive integer. Please try again.\n')
        except:
            print('Input was not a positive integer. Please try again.\n')
    return create_random_dates(num_birthdays)


def create_list_of_days(list_of_months):
# def create_list_of_days
#
# Objective:
#            Generate a list of randomly generated days (as ints) of the month based on the month of the year
#
# Inputs:
#            list_of_months - list of numbers [1,12] symbolizing month of the year
#
# Outputs:
#            list_of_days - int list of days corresponding to each month
#

    list_of_days = []
    for x in list_of_months:
        if x in [1, 3, 5, 7, 8, 10, 12]:
            list_of_days.append(random.randint(1,31))
        elif x in [4, 6, 9, 11]:
            list_of_days.append(random.randint(1,30))
        else:
            list_of_days.append(random.randint(1,28))
    return list_of_days


def return_random_dates_as_strings(list_of_months, list_of_days):
# def return_random_dates_as_strings
#
# Objective:
#            Combine int lists of months and days into a string list of dates
#
# Inputs:
#            list_of_months - int list of months
#            list_of_days   - int list of days
#
# Outputs:
#            date_strings - list of dates saved as strings
#
    
    
    months = ['January',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December']
    date_strings = []
    for count, value in enumerate(list_of_months):
        date_strings.append('{} {}'.format(months[value-1], list_of_days[count]))
    return date_strings
        
def create_random_dates(num_birthdays):
# def create_random_dates(num_birthdays)
#
# Objective:
#            Takes a number n and generates a string list of dates n long
#
# Inputs:
#            num_birthdays - number of birthdays (specified by user)
#
# Outputs:
#            date_strings - list of dates saved as strings
#
    
    list_of_months = [random.randint(1,12) for i in range(num_birthdays)]
    list_of_days = create_list_of_days(list_of_months)
    date_strings = return_random_dates_as_strings(list_of_months, list_of_days)
    return date_strings
        
def sum_identical_birthdays(date_strings):
# def sum_identical_birthdays(date_strings)
#
# Objective:
#            Return number of birthdays shared by 2 or more people in date_strings
#
# Inputs:
#            date_strings - list of randomly generated birthdays
#
# Outputs:
#            len(common_birthdays) - number of birthdays shared by 2 or more people in date_strings
#
    
    common_birthdays = set(i for i in date_strings if date_strings.count(i) >  1)
    return len(common_birthdays)

def monte_carlo(birthdays):
# def monte_carlo
#
# Objective:
#            Create 100,000 Monte Carlo (MC) runs of the randomly generated birthday list to 
#            find number of 
#
# Inputs:
#            birthdays - list of birthday dates (strings), months (ints), or days (ints)
#
# Outputs:
#            none
#
    
    num_birthdays = len(birthdays)
    print('Generating {} birthdays 100,000 times.'.format(num_birthdays))
    input('Press Enter to begin...')
    occurrences_of_shared_birthdays = 0;
    for x in range(100000):
        if ((x+1)%10000 == 0):
            print('Completed {} Monte Carlo runs.'.format(x+1))
        date_strings = create_random_dates(num_birthdays)
        if sum_identical_birthdays(date_strings) > 0:
            occurrences_of_shared_birthdays += 1
    percentage = str(round(100*occurrences_of_shared_birthdays/100000, 2))
    print('In {}/100000 ({}%) Monte Carlo runs of {} birthdays, at least two people shared a birthday.'.format(occurrences_of_shared_birthdays, percentage, num_birthdays))
            
    
def main():
    birthdays = generate_first_set_of_birthdays()
    num_identical_bdays = sum_identical_birthdays(birthdays)
    print('There were {} days where people shared identical birthdays.'.format(num_identical_bdays))
    monte_carlo(birthdays)
    
if __name__ == '__main__':
    main()
