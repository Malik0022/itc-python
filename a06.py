## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def is_prime(number):

    if type(number) != int:
        return False
    
    elif (number <= 1):
        return False
    
    for i in range(2, number):
        if (number%i == 0):
            return False   
    return True

def output_prime_factors(number):

    number = round(number)
    
    if (number < 0):
        return False
    
    for i in range(2, number + 1):
        if is_prime(i) and ( number % i ) == 0:
            print(i)
            
        # if (i<6) and (i!=4):
        #     if (number%i == 0):
        #         print(i)
        # if (i%2!=0) and (i%3!=0) and (i%5!=0): 
        #     if (number%i == 0):
        #         print(i)

#### End OF MARKER
### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(n):
    
    if type(n) != int:
        return None
    
    i = 2
    prime = 0
    p = 0 

    while(p < n):
        if is_prime(i):
            prime = i
            p += 1

        i += 1
    return prime

# print(get_nth_prime(1))   
    # if (n == 1):
    #     return 2
    
    # elif (n == 2):
    #     return 3
    
    # for i in range(n+1):
        
    #     if (i%2!=0):
    #         if(i%3!=0):
    #             sum =sum+1
    #             if (sum == n):
    #                 print(i)

    


    

    
#### End OF MARKER

