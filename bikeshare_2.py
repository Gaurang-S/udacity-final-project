import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
DAY_DATA = {  
              'monday': 1,
              'tuesday': 2,
              'wednesday': 3,
              'thursday': 4,
              'friday': 5,
              'saturday': 6,
              'sunday': 7,
              'all': 8
            }
MONTH_DATA = { 'january': 1,
               'february': 2,
               'march': 3,
               'april': 4,
               'may': 5,
               'june': 6,
               'july': 7,
               'august': 8,
               'september': 9,
               'october': 10,
               'november': 11,
               'december': 12,
               'all': 13
             }
            
def get_filters():
    """
    
    Asks user to specify a city, month, and day to analyze.
    city = input("Please enter a city:")
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    import sys
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please enter the city you want to explore. chicago, new york or washington? \n')
        if city not in CITY_DATA:
            restart = input("Invalid input. Do you want to restart? Enter y or n.\n")
            if restart.lower():
                main()
            elif restart.lower():
                sys.exit()
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)'
    while True:
        month = input('Please enter the month. all, january, february? \n')
        if month not in MONTH_DATA:
            restart = input("Invalid input. Do you want to restart? Enter y or n. \n")
            if restart.lower() == "y":
                main()
            elif restart.lower() == "n":
                sys.exit()
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter the day. all, monday, tuesday? \n')
        if day not in DAY_DATA:
            restart = input("Invalid input. Do you want to restart? Enter y or n.\n")
            if restart.lower() == "y":
                main()
            elif restart.lower() == "n":
                sys.exit()
        else:
            break
    
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
    df['filter_month'] = df['Start Time'].dt.month
    df['filter_day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    if month != "all":
        month_ref = MONTH_DATA[month]
        print(month_ref)
        df = df[df['filter_month'] == month_ref]
    if day != "all":
        day_ref = DAY_DATA[day]
        print(day_ref)
        df = df[df['filter_day'] == day_ref]
    #print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['filter_month'].mode()[0]
    print("\n The most popular month is " + str(popular_month))
    #print(MONTH_DATA['1'])
    # TO DO: display the most common day of week
    popular_day = df['filter_day'].mode()[0]
    print("\n The most popular day of the week is " + str(popular_day))
 
   # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    if popular_hour >= 12:
        print("\n The most popular hour is " + str(popular_hour - 12) + " PM")
    else:
        print("\n The most popular hour is " + str(popular_hour) + " AM")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(" \n The most popular starting station is " + popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(" \n The most popular ending station is " + popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + "_" + df['End Station']
    popular_comb = df['Combination'].mode()[0]
    st, en = popular_comb.split("_")
    print(" \n The most popular combination of stations is \n" + "Start Station: " + st + "\nEnd Station: " + en)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['travel_time'] = df['End Time'] - df['Start Time']
    
    # TO DO: display total travel time
    total_travel_time = df['travel_time'].sum()
    print("\nThe total travel time is ", str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['travel_time'].mean()
    print("\nThe mean travel time is ", str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("\nThere are " + str(user_type_counts) + " different user types.\n")
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nThere are " + str(gender_counts) + " different gender. \n")
          

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        latest_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print("\nThe earliest year of birth is " + str(earliest_birth))
        print("\nThe most recent year of birth is " + str(latest_birth))
        print("\nThe most common year of birth is " + str(most_common_birth))          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    i = 0
    while True:
        inp = input("\nDo you want to view the raw data? Enter y or n.\n")
        if inp == "y":
            print(df.iloc[i:i+5])
            i = i+5
        else:
            break
            
            
        
    
    
def main():
    while True:
        city, month, day = get_filters()
        #city, month, day = "chicago", "january", "monday"
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
            break
        
if __name__ == "__main__":
	main()
