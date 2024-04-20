## IMPORTS GO HERE

## END OF IMPORTS
### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(results):

    # It handles none error ---->>
    if results is None :
        return None
        
    # All name,rollno and sum of student we give it to this list --->>
    cumulative_marks=[]
    
    for result in results:
        # Initializing variable sum from 0 for each student ---->>
        total_score = 0
        student_roll_no = result[0]
        student_name = result[1]

        for scores in result[2:]:
            # It handles the if we through none in the sum it handles --->>
            if scores is not None:
                total_score += scores
            
        cumulative_marks.append((student_roll_no,student_name,total_score))
    
    return cumulative_marks

def find_top_student(results):
    
    top_students = []
    top_score = 0
    top_student_id = 0
    top_student_name = 0
    cumulative_marks = find_cumulative_marks(results)

    for student_id,student_name,scores in cumulative_marks:

        if scores > top_score:
            top_student_id = student_id
            top_student_name = student_name
            top_score = scores
            top_students = [(top_student_id,top_student_name)]

        elif scores == top_score:
            top_students.append((student_id,student_name))
    
    if len(top_students) == 1:
        return top_students[0]
    else:
        return top_students
        
# #### End OF MARKER
# if __name__ == '__main__':
#     results = [
#         ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
#         ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
#          ('p101113', 'Tamleek Ali', 87, None, 1.6)
#     ]
# # print(find_cumulative_marks(results))
# # #     # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]
# print(find_top_student(results))
    # output: ('p101111', 'Ali Khayam')
