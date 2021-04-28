import pandas as pd
import numpy as np
import pickle

'''
From the docs: List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
'''


########## Uncomment lines below to subset scrabble data frame
# scrabble = pd.read_csv('data/scrabble_games.csv')
# scrabble['date'] = pd.to_datetime(scrabble['date'])
# scrabble = scrabble[scrabble['date'] > '2016']
# 
# with open('data/scrabble_201617.p', 'wb') as write_file:
#     pickle.dump(scrabble, write_file)
#########

with open('data/scrabble_201617.p', 'rb') as read_file:
    scrabble = pickle.load(read_file)

'''
A list comprehension creates a new list out of an iterable.  Instead of creating an empty list outside of a for-loop which you populate with `.append` or `.extend`, you can often do the same thing in one line.

For an example, let's create a new list which consists of the years of the Scrabble games in the dataset.  To do so, we could use a for loop like so.
'''

date_list = list(scrabble['date'])

years = []
for date in date_list:
    years.append(date[:4])

print(np.unique(years, return_counts=True))

'''
We can see from the value counts that we have 40,696 games that occured in 2016, and 6,764 that occured in 2017
'''

'''
Now let's reproduce that result with a list comprehension.
Fill in the list comprehension below with the appropriate code.
The first fill should be the operation you want to perform (slicing the list). The second should be a variable name assigned to represent each element of the iterable.  The last should be the iterable you want to iterate over.
'''

years_list_comp = [ "Fill" for fill  in [] ]

#__SOLUTION__
years_list_comp = [date[:4] for date in date_list]

assert years == years_list_comp
print('Correct. The list comprehension creates the same list.')

'''
We can perform any operation which can receive the type of element in the list as an argument.

Let's now use the `pd.to_datetime()` to convert the dates in date_list to date_time_objects.
'''

dates_datetime = []
#__SOLUTION__
dates_datetime = [pd.to_datetime(date) for date in date_list]

assert type(np.random.choice(dates_datetime)) ==  type(pd.to_datetime('2020-04-26'))
print("Correct. All of the objects are now datetime objects.")

'''
List comprehension can also use logic.  Before the `for` keyword, you can add `if-else` statements to regulate which elements are selected.
'''

print(f'''
The 95th percentile of player ratings of players who lost a game is {scrabble['loseroldrating'].quantile(.95)}
Create a list of booleans for each element, where True represents loseroldratings whose rating is greater than or equal to the 95th percentile, and False is less than the 95th percentile.
''')

lor = list(scrabble['loseroldrating'])
ninetyfifth_p =  scrabble['loseroldrating'].quantile(.95)

lor_95 = []


#__SOLUTION__
lor_95 = [True if rating >= ninetyfifth_p
               else False for rating in lor]

assert sum(lor_95) == 2379
print('Correct')

'''
We can also use the `zip` operator in list comprehensions.  This requires two variable names in the `for` clause of the statement.

Use `zip` and a list comprehension to make a new list comprised of the difference between `winneroldrating` and `loseroldrating`.
'''

wor = list(scrabble['winneroldrating'])
lor = list(scrabble['loseroldrating'])

rating_difference = []

#__SOLUTION__
rating_difference = [w - l for w,l in zip(wor, lor)]

assert sum(rating_difference) == 4093066
print("Correct! Nice job.")
