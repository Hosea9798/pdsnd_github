import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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

    city = ''
    while True:
        city = input("\nPlease input city name: (ex. chicago, new york city, washington)\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("Sorry we don't find data. Please input either chicago, new york city or washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please input month: (ex.all, january, february, march, april, may, june)\n").lower()
    while month != 'all':
        if month == 'january':
            break
        if month == 'february':
            break
        if month == 'march':
            break
        if month == 'april':
            break
        if month == 'may':
            break
        if month == 'june':
            break
        print("Wrong input,please try again")
        month = input("which month do you want search?\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        "Please input weekday : (ex.all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n").lower()
    while day != 'all':
        if day == 'monday':
            break
        if day == 'tuesday':
            break
        if day == 'wednesday':
            break
        if day == 'thursday':
            break
        if day == 'friday':
            break
        if day == 'saturday':
            break
        if day == 'sunday':
            break
        print("Error input, please try again.\n")
        day = input("which weekday do you want search:?\n").lower()

    print('-' * 40)
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
    # use code
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is:', popular_month)

    # TO DO: display the most common day of week
    most_day_of_week = df['day'].mode()[0]
    print("Most common day_week:" + most_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    most_start_hour = df['hour'].mode()[0]
    print("Most common start hour:" + str(most_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    yesorno(df)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: " + most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: " + most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_fre_combin = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print(
        "The most frequent combination of start station and end station trip is : " + str(most_fre_combin.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    yesorno(df)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: " + str(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: " + str(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    yesorno(df)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("Count of user types: \n" + str(count_user_types))

    try:
        # TO DO: Display counts of gender
        count_gender = df['Gender'].value_counts()
        print("Count of user gender: \n" + str(count_gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_birth = df['Birth Year'].min()
        recent_year_birth = df['Birth Year'].max()
        common_year_birth = df['Birth Year'].mode()[0]

        print('Earliest birth: {}\n'.format(earliest_year_birth))
        print('Most recent birth: {}\n'.format(recent_year_birth))
        print('Most common birth: {}\n'.format(common_year_birth))
    except:
        print("Washington don't have gender and brith year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    yesorno(df)


def yesorno(df):
    choose = input("Do you want to check the first 5 rows of the dataset related to the chosen city?\n")
    i = 5
    while choose == 'yes':
        print(df.head(i))
        i += 5
        if input('Do you want to check another 5 rows of the dataset?') == "no":
            break

# This is the main def.
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

# This is the magic def.
if __name__ == "__main__":
    main()
