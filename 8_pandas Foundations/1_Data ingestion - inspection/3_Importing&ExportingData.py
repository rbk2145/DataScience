###Reading a flat file
# Read in the file: df1
df1 = pd.read_csv("world_population.csv")

# Create a list of the new column labels: new_labels
new_labels = ["year","population"]

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv('world_population.csv', header=0, names=new_labels)

# Print both the DataFrames
print(df1)
print(df2)


###Delimiters, headers, and extensions
# Read the raw file as-is: df1
df1 = pd.read_csv(file_messy)

# Print the output of df1.head()
print(df1.head())

# Read in the file with the correct parameters: df2
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment="#")

# Print the output of df2.head()
print(df2.head())

# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv(file_clean, index=False)

# Save the cleaned up DataFrame to an Excel file without the index
df2.to_excel('file_clean.xlsx', index=False)


###
