#list 
pop = [1.3, 2.1, 4.5]
countries = ["afghanistan","albania", "algeria"]
index_alb = countries.index("albania")
index_alb
pop[index_alb]

# in order compare to two lists is a big task
#dictionaries come {key: value}
data= {"afghan":1.3, "albania":2.1, "algeria":4.5}

####pratice 
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

#####
# 2 list into 1 dict
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = dict(zip(countries, capitals))

# Print europe
print(europe)

###
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe["norway"])
