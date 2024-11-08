grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Вычисление среднего балла
middle_grades = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),
sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]

# Сортировка студентов (в соответсвии с заданием - по алфавиту)
list_of_students = sorted(students)

# Объединение оценок и списка студентов

list_of_grades = zip(list_of_students,middle_grades)
grades_of_students = dict(list_of_grades)

print(grades_of_students)



