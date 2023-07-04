if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student=student_marks[query_name]
    marks_sum=0
    for marks in student:
        marks_sum+=marks
    
    print(format(marks_sum/len(student),'.2f'))
