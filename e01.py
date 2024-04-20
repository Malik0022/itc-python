## START OF get_diag_sum FUNCTION
def get_diag_sum(n):

    if n%2 == 0 :
        return None

    top_right = 0 
    top_left = 0
    top = 0 
    bottom = 0 
    diagonal_sum = 1

    for i in range(3,n+1,2):

        top_right = i**2    
        top_left = top_right - (i-1)
        top = top_left - (i-1)
        bottom = top - (i-1)

        diagonal_sum += top_right + top_left + top + bottom
    
    return diagonal_sum
## END OF MARKER
if __name__ == '__main__':   
    print (get_diag_sum(113))