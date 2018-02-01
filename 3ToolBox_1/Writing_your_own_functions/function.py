##What are the values in object1, object2, and object3, respectively?
object1 = "data" + "analysis" + "visualization"
object2 = 1 * 3
object3 = "1" * 3

##What are the types of x, y1, and y2?
y1 = str(x)
y2 = print(x)

##
# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations'+'!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()

###Write a simple function


###Single-parameter functions
# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')

####Functions that return single values
# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return
    return shout_word

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)










########








