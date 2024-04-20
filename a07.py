## IMPORTS GO HERE

## END OF IMPORTS
# ### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
def calculate_sgpa(grades):

    if grades == None:
        return None

    if not isinstance(grades, list):
        grades = [grades]


    total = len(grades)

    #  if the list is empty this condition handles it ....
    if total == 0:
        return False
    
    gpa = 0.0    

    for grade in grades:
        
        if grade =='A+':
            gpa += 4.00
        elif grade == 'A':
            gpa += 4.00
        elif grade == 'A-':
            gpa += 3.67
        elif grade == "B+":
            gpa += 3.33
        elif grade == 'B':
            gpa += 3.00
        elif grade == 'B-':
            gpa += 2.67
        elif grade == 'C+':
            gpa += 2.33
        elif grade == 'C':
            gpa += 2.00
        elif grade == 'C-':
            gpa += 1.67
        elif grade == 'D+':
            gpa += 1.33
        elif grade == 'D':
            gpa += 1.00
        else:
            return None

    sgpa = gpa /total
    return sgpa       
#### End OF MARKER
### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
credit_hours = [4.0,4.0,4.0,3.0,3.0,3.0,2.0,2.0,2.0,1.0,1.0]
def calculate_sgpa_weighted(grades, credit_hours):
    
    if not isinstance(grades, list):
        grades = [grades]

    # alternate method to check a grades a list or not ----->>
    # grades = [grades] if not isinstance(grades, list) else grades

    if not isinstance(credit_hours, list):
        credit_hours = [credit_hours]

    
    if len(grades) != len(credit_hours):
        return None
    
    # is new_list me har grade ko uska gradepoint milega ---->
    gpa_point = []
    total_gpa_points = 0

    # Add the total credit hours points in credit_hours list  ----->>
    total_credits_point = sum(credit_hours)

    for grade in grades:

        if grade == "A+":
            gpa_point.append(4.00)
        elif grade == "A":
            gpa_point.append(4.00)
        elif grade == "A-":
            gpa_point.append(3.67)
        elif grade == "B+":
            gpa_point.append(3.33)
        elif grade == "B":
            gpa_point.append(3.00)
        elif grade == "B-":
            gpa_point.append(2.67)
        elif grade == "C+":
            gpa_point.append(2.33)
        elif grade == "C":
            gpa_point.append(2.00)
        elif grade == "C-":
            gpa_point.append(1.67)
        elif grade == "D+":
            gpa_point.append(1.33)
        elif grade == "D":
            gpa_point.append(1.00)
        elif grade == "F":
            gpa_point.append(0.0)
        else:
            return None  
      
    # gpa_point list and credit hours list is multiplying together to get total gpa = ---->>>   
    for i in range(len(gpa_point)):
        total_gpa_points += gpa_point[i] * credit_hours[i]
    
    sgpa = total_gpa_points / total_credits_point
    return sgpa  
### End OF MARKER


if __name__ == '__main__':
    print(calculate_sgpa(['A+']))  
    print(calculate_sgpa_weighted(['A+'], [4]))
