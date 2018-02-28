####Extracting data with a MultiIndex
Print sales.loc[['CA', 'TX']]
print(sales.loc[["CA","TX"]])

###Setting & sorting a MultiIndex
# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)

####Using .loc[] with nonunique indexes
# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])

####Indexing multiple levels of a MultiIndex
# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY', 1), :]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA', 'TX'], 2), :]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None), 2), :]
