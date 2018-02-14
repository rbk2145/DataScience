###1
###pivoting data
# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=["Month", "Day"], columns="measurement", values="reading")

# Print the head of airquality_pivot
print(airquality_pivot.head())


###2
###Resetting the index of a DataFrame
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the new index of airquality_pivot
print(airquality_pivot.index)

# Print the head of airquality_pivot
print(airquality_pivot.head())



###3
###Pivoting duplicate values
# Pivot airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=["Month", "Day"], columns="measurement", values="reading", aggfunc=np.mean)

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())
