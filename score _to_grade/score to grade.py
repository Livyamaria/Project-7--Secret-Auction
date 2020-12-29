"""Write a program that converts their scores to grades.
 By the end of your program, you should have a new dictionary called student_grades
 that should contain student names for keys and their grades for values. """
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,}

student_grades={}


for keys in student_scores:
  if student_scores[keys]>=91:
    student_grades[keys]="Outstanding"
  elif student_scores[keys]>=81:
     student_grades[keys]="Exceeds Expectations"
  elif student_scores[keys]>=71:
     student_grades[keys]="Acceptable"
  else :
     student_grades[keys]="Fail"

print(student_grades)



