###pandas line plots
# Create a list of y-axis column names: y_columns
y_columns = ["AAPL","IBM"]

# Generate a line plot
df.plot(x="Month", y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()


###pandas scatter plots
## data https://archive.ics.uci.edu/ml/datasets/Auto+MPG
# Generate a scatter plot
df.plot(kind="scatter", x='hp', y='mpg', s=sizes)

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()


###pandas box plots
##https://archive.ics.uci.edu/ml/datasets/Auto+MPG
# Make a list of the column names to be plotted: cols
cols = ['weight', 'mpg']

# Generate the box plots
df[cols].plot(kind='box', subplots=True)

# Display the plot
plt.show()



###pandas hist, pdf and cdf
##data from https://github.com/mwaskom/seaborn-data/blob/master/tips.csv
# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', normed=True, bins=30, range=(0,.3))
plt.show()

# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', normed=True, cumulative=True, bins=30, range=(0,.3))
plt.show()
