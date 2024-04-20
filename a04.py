## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade ( total_marks ):

    total_marks = round( total_marks )

    if total_marks >= 90:
        return 'A+'
    elif total_marks >= 86:
        return 'A'
    elif total_marks >= 82:
        return 'A-'
    elif total_marks >= 78:
        return 'B+'
    elif total_marks >= 74:
        return 'B'
    elif total_marks >= 70:
        return 'B-'
    elif total_marks >= 66:
        return 'C+'
    elif total_marks >= 62:
        return 'C'
    elif total_marks >= 58:
        return 'C-'
    elif total_marks >= 54:
        return 'D+'
    elif total_marks >= 50:
        return 'D'
    elif total_marks <= 49:
        return 'F'
        
    elif total_marks >= 0:
        return 'F'
    
get_grade(90)


# #### End OF MARKER
def get_point_equiv( grade ):

    if grade == 'A' or grade == 'A+':
        return 4.00
    
    elif grade == 'A-':
        return 3.67

    elif grade == 'B+':
        return 3.33

    elif grade == 'B':
        return 3.00

    elif grade == 'B-':
        return 2.67

    elif grade == 'C+':
        return 2.33

    elif grade == 'C':
        return 2.00

    elif grade == 'C-':
        return 1.67

    elif grade == 'D+':
        return 1.33

    elif grade == 'D':
        return 1.00
    
    else:
        return 0.0
    

# #### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####

def calculate_sgpa ( grade1, grade2 , grade3 ):

    total_sbj = 0
    
    if grade1 != "nothing":
        total_sbj += 1

    if grade2 != "nothing":
        total_sbj += 1

    if grade3 != "nothing":
        total_sbj += 1

    grade1 = get_point_equiv(grade1)
    grade2 = get_point_equiv(grade2)
    grade3 = get_point_equiv(grade3)

    sgpa = (grade1 + grade2 + grade3) / total_sbj
    return sgpa

#### End OF MARKER
# print (get_grade(90))
# print (get_point_equiv('B'))
# print (calculate_sgpa('A','C','F'))

    