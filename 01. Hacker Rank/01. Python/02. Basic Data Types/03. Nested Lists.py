def sort_students(names_scores):
    scores = []                                                           ## list to store only scores of student
    for student in names_scores:
        scores.append(student[1])                                         ## retrieving score of each students
        
    sorted_scores = sorted(set(scores))             ## sorting and creating unique values of scores, set is used to select unique vaues from the list and sort is used to sort the list
    second_lowest_score = sorted_scores[1]          ## finding the secoond lowest value in the list
    
    names_second_lowest = []                                              ## list to store the names of second lowest score names
    for student in names_scores:
        if student[1] == second_lowest_score:                             ## compairing the scores of each student's scores with second last scores
            names_second_lowest.append(student[0])                        ## fetching the names of the second last scores students
    names_second_lowest = sorted(names_second_lowest)                     ## sorting the names in alphabetical order
    
    for name in names_second_lowest:
        print(name)                                                       ## printing the Names of students who got second last scores



if __name__ == '__main__':
    names_scores = []                                                    ## creating list to store names and score os student
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores.append([name, score])                               ## appending list of name and score of student in names_score list
        


        
    sort_students(names_scores)                                          ## calling sort_student function