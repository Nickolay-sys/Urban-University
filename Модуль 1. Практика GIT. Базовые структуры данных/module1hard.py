grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
the_average_grades_score = [sum(grades[0])/len(grades[0]),
                            sum(grades[1])/len(grades[1]),
                            sum(grades[2])/len(grades[2]),
                            sum(grades[3])/len(grades[3]),
                            sum(grades[4])/len(grades[4])]
list_of_average_score_for_each_student = {sorted_students[0]: the_average_grades_score[0],
                                          sorted_students[1]: the_average_grades_score[1],
                                          sorted_students[2]: the_average_grades_score[2],
                                          sorted_students[3]: the_average_grades_score[3],
                                          sorted_students[4]: the_average_grades_score[4]}
print(list_of_average_score_for_each_student)

class Example:
    grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
    students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
    def __init__(self):
        sort_stud = sorted(self.students)
        avg_grades = []
        for i in self.grades:
            avg = sum(i)/len(i)
            avg_grades.append(avg)
        dict_ = dict(zip(sort_stud,avg_grades))
        print(dict_)
Example()

    

