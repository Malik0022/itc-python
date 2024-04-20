## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(number):

    if type(number) != int:
        return False
    
    elif (number <= 1):
        return False
    
    for i in range(2, number):
        if (number%i == 0):
            return False   
    return True
        
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(x):
    
    # print(f"Factors of {x} are:")
    for i in range(1,x+1):
        if (x%i == 0):
           print(i)
    
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(num):

    num = int(num)
    for i in range(num,0,-1):
        if is_prime(i):
            return i
        
    return None

print(get_largest_prime(15))
     

#### End OF MARKER

# if __name__ == '__main__':

    # print is_prime(499)  # should return True

    # print get_largest_prime(10)  # should return 7
    # # print get_largest_prime(100000)  # bonus, try with 100k

    # output_factors(10)  # should output -- 1 2 5 10 -- one on each line





