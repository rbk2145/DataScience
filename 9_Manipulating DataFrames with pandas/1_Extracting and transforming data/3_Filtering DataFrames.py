###Thresholding data
# Create the boolean array: high_turnout
high_turnout = election["turnout"]>70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election.loc[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)


###Filtering columns using other columns
# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election['margin'] < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.loc[too_close, 'winner'] = np.nan

# Print the output of election.info()
print(election.info())


###Filtering using NaNs
#http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.html
# Select the 'age' and 'cabin' columns: df
df = titanic[['age','cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)

# Drop columns in titanic with more than 1000 missing values
print(titanic.dropna(thresh=1000, axis='columns').info())


