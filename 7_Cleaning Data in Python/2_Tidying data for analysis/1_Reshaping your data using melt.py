###1
# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=df, id_vars=["Month","Day"])

# Print the head of airquality_melt
print(airquality_melt.head())


###2
###Customizing melted data
# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=df, id_vars=["Month", "Day"], var_name="measurement", value_name="reading")

# Print the head of airquality_melt
print(airquality_melt.head())


###3
###
