import random
    
def create_random_birthdays():
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
    list_of_months = [random.randint(1,12) for i in range(num_birthdays)]
    list_of_days = create_list_of_days(list_of_months)
    date_strings = return_random_dates_as_strings(list_of_months, list_of_days)
    return date_strings


def create_list_of_days(list_of_months):
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
        
        
def sum_identical_birthdays(date_strings):
    common_birthdays = set(i for i in date_strings if date_strings.count(i) >  1)
    return len(common_birthdays)

def monte_carlo(birthdays):
    num_birthdays = len(birthdays)
    print('Generating {} birthdays 100,000 times.'.format(num_birthdays))
    input('Press Enter to begin...')
    occurrences_of_shared_birthdays = 0;
    for x in range(100000):
        if ((x+1)%10000 == 0):
            print('Completed {} Monte Carlo runs.'.format(x+1))
        list_of_months = [random.randint(1,12) for i in range(num_birthdays)]
        list_of_days = create_list_of_days(list_of_months)
        date_strings = return_random_dates_as_strings(list_of_months, list_of_days)
        if sum_identical_birthdays(date_strings) > 0:
            occurrences_of_shared_birthdays += 1
    percentage = str(round(100*occurrences_of_shared_birthdays/100000, 2))
    print('In {}/100000 ({}%) Monte Carlo runs of {} birthdays, at least two people shared a birthday.'.format(occurrences_of_shared_birthdays, percentage, num_birthdays))
            
    
# def main():
#     num_birthdays = get_num_birthdays()
#     list_of_months = [random.randint(1,12) for i in range(num_birthdays)]
#     list_of_days = create_list_of_days(num_birthdays, list_of_months)
#     return_random_dates(list_of_months, list_of_days)
    
# if __name__ == '__main__':
#     main()
    
birthdays = create_random_birthdays()
num_identical_bdays = sum_identical_birthdays(birthdays)
print('There were {} days where people shared identical birthdays.'.format(num_identical_bdays))
monte_carlo(birthdays)
