###Visualizing single variables with histograms
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()


###Visualizing multiple variables with boxplots
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
df.boxplot(column="initial_cost", by="Borough",rot=90)

# Display the plot
plt.show()



##3Visualizing multiple variables with scatter plots
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create and display the first scatter plot
df.plot(kind="scatter", x="initial_cost", y="total_est_fee", rot=70)
plt.show()

# Create and display the second scatter plot
df_subset.plot(kind="scatter", x="initial_cost", y="total_est_fee", rot=70)
plt.show()
