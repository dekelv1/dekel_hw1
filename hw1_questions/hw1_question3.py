math_grades= {
    "Dekel": ("Math",100,90),
    "Alon": ("Math",80,90),
    "Motti": ("Math",50,60),
    "Or": ("Math",87,77),
    "Mickey": ("Math",75,95),
    "Nataly": ("Math",60,60)
}
history_grades= {
    "Dekel": ("History",70,75),
    "Alon": ("History",100,98),
    "Motti": ("History",93,87),
    "Or": ("History",50,62),
    "Mickey": ("History", 80,92)

}

def compare_subjects_within_student (subj1_all_students,subj2_all_students):
    for student in subj1_all_students: 
        tuple1 = subj1_all_students[student]
        mean_grade1 = (tuple1[1] + tuple1[2])/2
        
        if student in subj2_all_students.keys():
            tuple2 = subj2_all_students[student]
            mean_grade2= (tuple2[1] + tuple2[2])/2
            if mean_grade1 > mean_grade2:
                print(student, tuple1[0])
            else: 
                print(student, tuple2[0])

if __name__ == '__main__':
    # Question 3
    param1 = math_grades
    param2 = history_grades
    compare_subjects_within_student(math_grades, history_grades)
