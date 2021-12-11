import random
    
def get_num_birthdays():
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
    return num_birthdays

def create_list_of_days(num_birthdays, list_of_months):
    list_of_days = []
    
    for x in range(num_birthdays):
        if list_of_months[x] in [1, 3, 5, 7, 8, 10, 12]:
            list_of_days.append(random.randint(1,31))
        elif list_of_months[x] in [4, 6, 9, 11]:
            list_of_days.append(random.randint(1,30))
        else:
            list_of_days.append(random.randint(1,28))
            
    return list_of_days

def return_random_dates(list_of_months, list_of_days):
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
    
    print('Here are {} random birthdays: '.format(len(list_of_months)))
    
    for x in range(len(list_of_months)):
        print('{} {}'.format(months[list_of_months[x]-1], list_of_days[x]))
    
def main():
    num_birthdays = get_num_birthdays()
    list_of_months = [random.randint(1,12) for i in range(num_birthdays)]
    list_of_days = create_list_of_days(num_birthdays, list_of_months)
    return_random_dates(list_of_months, list_of_days)
    
if __name__ == '__main__':
    main()