import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
answer = ['yes','no']
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
    citys=['chicago','new york city','washington']
   
    while True :
        city= input("Please , select the city  ( chicago, new york city, washington)\n ==> ").lower() 
       
        if city  in citys:
            break
            
        else:
            print('please enter a valid city ( make sure that the letters of the word are spelled correctly)')

    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january' , 'february' ,'march' ,'april', 'may' , 'june' , 'all']    
    while True :
        month= input('which month (January , February , March , April , May , June , all) )\n ==> ').lower()
        if month in months :
            break
        else :
            print(' enter a valid month (Please make sure that the letters of the word are spelled correctly)')

    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['satuarday','sunday','munday','tuesday','wednesday''thursday','friday','all']
    while True :
        day = input('which day woud you like ( Saturday , Sunday , Munday , Tuesday , Wednesday , Thursday , Friday ,all)\n ==>').lower()  
        if day in days :
            break
        else:
            print("invalid day (Please make sure that the letters of the word are spelled correctly)")   


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
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


   


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    PopMonth = df['month'].mode()[0]

    print('The Most Popular Month Is :{} '.format(PopMonth))


    # TO DO: display the most common day of week
    PopDayOfWeek = df['day_of_week'].mode()[0]

    print('The Most Day Of Week Is :{}' .format(PopDayOfWeek))

    # TO DO: display the most common start hour
    PopCommonStartHour = df['hour'].mode()[0]

    print('The Most Common Start Hour is :{} '.format(PopCommonStartHour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    PopStartStation = df['Start Station'].mode()[0]

    print('The Most Popular Start Station :{}'.format(PopStartStation))

    # TO DO: display most commonly used end station
    PopEndStation = df['End Station'].mode()[0]

    print(' The Most End Station Is :{} '.format(PopEndStation))


    # TO DO: display most frequent combination of start station and end station trip
    df['line'] = df['Start Station']+","+df['End Station']
    
    line = df['line'].mode()[0]
                                           
    print('The Most Common Line is : {}'.format(line))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TotalTravelTime = df['Trip Duration'].sum().round()
    print('Total Travel Time:{} Seconds '.format(TotalTravelTime))



    # TO DO: display mean travel time
    MeanTravelTime = df['Trip Duration'].mean().round()
    print('Mean Travel Time:{} Seconds '.format(MeanTravelTime))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        
        # Display counts of gender
        
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        
        # Display earliest, most recent, and most common year of birth
        
        print('Birth Year Stats: ----')
        
        EarliestYear = int(df['Birth Year'].min())
        print('Earliest Year:{}'.format(EarliestYear))
        
        MostRecentYear = int(df['Birth Year'].max())
        print('Most Recent Year:{}'.format(MostRecentYear))
        
        MostCommonYear = int( df['Birth Year'].mode()[0])
        print('Most Common Year:{}'.format(MostCommonYear))
        
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    """in this function we ask the user if he or she want to display data """
    respons=input('Would you like to display data ? \n==> ')
    if respons.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count:count+5])
            count +=5
            ask =input('need more , answer yes or no \n ==>')
            while ask.lower() not in answer :
                 print('please enter a valid answer')
                 ask =input('need more , answer yes or no ,  please \n ==>')
            if ask.lower() == 'no':
                 break
                       
        
                   
def main():
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no ?.\n ==>')
        while restart.lower() not in answer:
              print('enter a valid input')
              restart = input('\nWould you like to restart? Enter yes or no ?.\n ==>')
        if restart.lower()== 'no':
            break
            


if __name__ == "__main__":
    main()
