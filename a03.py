# ## IMPORTS GO HERE
# ## END OF IMPORTS
# #### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x,guess=1.1):
 
    if x<0:
        return None
    if good_enough(guess,x):
        return guess
    else:
        new_guess=improve_guess(guess,x)
        return sqrt(x,new_guess)
        
def good_enough(guess,x):

    if abs(guess*guess-x)<0.1:
        return True
    else:
        return False
# #### End OF MARKER
# #### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(x, y):

    arithmetic_mean = (x + y) / 2
    return arithmetic_mean
# #### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(a , x):
    
        x=x*1.0
        better_guess = average(a,x/a)
        return better_guess
# #### End OF MARKER
print(sqrt(36,5.8))   

if 