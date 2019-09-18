import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = []
    while city == []:
        for c in ['Chicago', 'New York City', 'Washington']:
            inp = input("Would you like to see data for {}? Y for Yes or N for No.\n".format(c)).lower()
            while inp not in ['y', 'n']:
                inp = input('Something might be wrong in the input. Please only type Y or N.\n').lower()
            if inp == 'y':
                city.append(c.lower())
        if city == []:
            print('Please select at least one city.')

    # TO DO: get user input for month (all, january, february, ... , june)
    print("What months would you like to see? Please input intergers from 1 to 12, using space to separate if needed. If you'd like to see data for all months, please input 'all'.\n")
    test = False
    while test == False:
        test = True
        month = input().lower()
        if month == "all":
            month = list(range(1, 13))
        elif month == '':
            test = False
        else:
            try:
                month = list(map(int, month.split()))
                for m in month:
                    if m not in range(1,13):
                        test = False
            except:
                test = False
        if test == False:
            print('Something might be wrong in the input. Please only type "all" or intergers from 1 to 12, using space to separate if needed.\n')
    month = np.unique(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("What days of week would you like to see?\nPlease input integers from 0 to 6, using space to separate if needed.\nThe corresponding days of week are as follows:\n0 Monday\n1 Tuesday\n2 Wednesday\n3 Thursday\n4 Friday\n5 Saturday\n6 Sunday\nIf you'd like to see data for all days, please input 'all'.\n")
    test = False
    while test == False:
        test = True
        day = input().lower()
        if day == "all":
            day = list(range(7))
        elif day == '':
            test = False
        else:
            try:
                day = list(map(int, day.split()))
                for d in day:
                    if d not in range(7):
                        test = False
            except:
                test = False
        if test == False:
            print('Something might be wrong in the input. Please only type "all" or intergers from 0 to 6, using space to separate if needed.\n')
    day = np.unique(day)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df_city = pd.DataFrame()
    for c in city:
        df_city = df_city.append(pd.read_csv(CITY_DATA[c]))
    df_city['Start Time'] = pd.to_datetime(df_city['Start Time'])
    df_city['month'] = df_city['Start Time'].dt.month
    df_city['day_of_week'] = df_city['Start Time'].dt.dayofweek
    
    df_month = pd.DataFrame()
    for m in month:
        df_month = df_month.append(df_city[df_city['month'] == m])
        
    df = pd.DataFrame()
    for d in day:
        df = df.append(df_month[df_month['day_of_week'] == d])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', months[common_month - 1])

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', days_of_week[common_day])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_sta_sta = df['Start Station'].mode()[0]
    print('Most commonly used start station:', com_sta_sta)

    # TO DO: display most commonly used end station
    com_end_sta = df['End Station'].mode()[0]
    print('Most commonly used end station:', com_end_sta)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + '-' + df['End Station']
    fre_com = df['combination'].mode()[0].split('-')
    print('Most frequent combination of start station and end station trip: from {} to {}'.format(fre_com[0], fre_com[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time:', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_count = df['User Type'].value_counts()
    print('Counts of user types:')
    print(type_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nCounts of genders:')
        print(gender_count)
    except KeyError:
        print("\nOoops...there isn't the data of genders for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nThe earliest, most recent, and most common years of birth: {}, {}, {}'.format(earliest_year, recent_year, common_year))
    except KeyError:
        print("\nOoops...there isn't the data of birth years for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
