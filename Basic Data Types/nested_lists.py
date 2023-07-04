if __name__ == '__main__':
   
    names_scores=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores.append(list([name,score]))
        scores.append(score)
        
    scores.sort()
    
    ind_scores=[]
    for i in scores:
        ind_score=scores.index(i)
        if ind_score not in ind_scores:
            ind_scores.append(ind_score)

    names_second_lowest_students=[]
    for student in names_scores:
        if student[1]==scores[ind_scores[1]]:
            names_second_lowest_students.append(student[0])
            
    names_second_lowest_students.sort()
    for name in names_second_lowest_students:
        print(name)
