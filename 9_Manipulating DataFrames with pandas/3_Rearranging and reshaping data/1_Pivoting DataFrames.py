###Pivoting a single variable
# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index="weekday",columns="city",values="visitors")

# Print the pivoted DataFrame
print(visitors_pivot)


###Pivoting all variables
# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index='weekday', columns='city', values='signups')

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index='weekday', columns='city')

# Print the pivoted DataFrame
print(pivot)


###
