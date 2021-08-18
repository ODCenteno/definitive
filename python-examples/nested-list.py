if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        python_students.append(student)
        
    scores_list = [student[1] for student in python_students]
    scores_list_without_min = scores_list.pop(min(scores_list))
    scores_list_without_min = sorted(scores_list_without_min)
    
    second_lowest = scores_list_without_min[0]
    
    names_lowest = []
    
    for students in python_students:
        if second_lowest in students:
            names_lowest.append(students[0])
            
    names_lowest.sort
    for name in names_lowest:
        print(name)