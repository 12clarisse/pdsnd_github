import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    print('Which city would you like to see data for?')
    city = input('Put the name of the city for which you want to see data: ').lower()
    
    while city not in CITY_DATA:
        city = input('This is incorrect, select one of the following city chicago, new york city, washington: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    print('Which month do you want to use?')
    month = input('Put the month name: ').lower()
    
    while month not in ['january','february','march','april','may','june']:
        month = input('This is incorrect, select another month or rewrite the month: ').lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day do you want to use?')
    day = input('Put the day name: ').lower()
    
    while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input('This is incorrect, rewrite the day: ').lower()

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
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: {}'.format(df['month'].mode()[0]))
    
    # TO DO: display the most common day of week
    print('The most common day of week is: {}'.format(df['day_of_week'].mode()[0]))
    
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    print('The most common hour is: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode()[0]))
    
    # TO DO: display most frequent combination of start station and end station trip
    df['entire_journey'] = df['Start Station']+ "-" + df['End Station']
    print('The most frequent combination is: {}'.format(df['entire_journey'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['travel_duration'] = df['End Time'] - df['Start Time']

    # display total travel time
    print('The total travel time is: {}'.format(df['travel_duration'].sum()))
    # display mean travel time
    print('The mean travel time is: {}'.format(df['travel_duration'].mean()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The count of user types is: ', df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if city != 'washington':
        print('The count of gender is: {}'.format(df['Gender'].value_counts()))
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('The earliest year is: {}'.format(int(df['Birth Year'].min())))
        print('The most recent year is: {}'.format(int(df['Birth Year'].max())))
        print('The most common year is: {}'.format(int(df['Birth Year'].mode()[0])))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """
    count = 0

    while True:
        # Check if response is yes, print the raw data and increment count by 5
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer == 'yes':
            print(df.iloc[count])
            count += 5
           
        # otherwise break
        if answer == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
