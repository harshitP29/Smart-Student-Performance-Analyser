# smart student performance analyzer using python

n = int(input("enter the number of students: "))
students = []
for i in range(n):
    print("\n========================================")
    print("          STUDENT PERFORMANCE")
    print("========================================")

    name=input("Enter the name of student: ")
    physics = float(input("Enter the marks of physics (0-100) "))
    chemistry = float(input("Enter the marks of chemistry (0-100): "))
    maths = float(input("Enter the marks of maths (0-100): "))
    english=float(input("Enter the marks of english (0-100): "))
    hindi = float(input("Enter the marks of hindi (0-100): "))

    total_marks= physics+chemistry+maths+english+hindi
    percentage= total_marks/5

    print("\n---------- STUDENT REPORT ----------")

    print("\nstudent name : ", name)
    print("physics marks : ", physics)
    print("chemistry marks: ", chemistry)
    print("maths marks: ", maths)
    print("english marks: ", english)
    print("hindi marks: ", hindi)
    print("total marks: ", total_marks)
    print("percentage: ", percentage)

    if(percentage>=90):
        print("A+ grade")
    
    elif(percentage>=80):
        print("A grade")
        
    elif(percentage>=70):
        print("B grade")

    elif(percentage>=60):
        print("C grade")

    elif(percentage>=50):
        print("D grade")
        
    else:
        print("F grade")

    if physics < 30 or chemistry < 30 or maths < 30 or english < 30 or hindi < 30:
        result = "FAIL"
    else:
        result = "PASS"

    print("\nOverall Result:", result)

    student = [name, physics, chemistry, maths, english, hindi, total_marks, percentage, result]
    students.append(student)
        

    largest = physics
    strong_subject = "physics"
    if chemistry>largest:
        largest = chemistry
        strong_subject = "chemistry"

    if maths>largest:
        largest = maths
        strong_subject = "maths"

    if english>largest:
        largest= english
        strong_subject = "english"

    if hindi>largest:
        largest= hindi
        strong_subject = "hindi"

    strong_subjects = []

    if physics == largest:
        strong_subjects.append("physics")

    if chemistry == largest:
        strong_subjects.append("chemistry")

    if maths == largest:
        strong_subjects.append("maths")

    if english == largest:
        strong_subjects.append("english")

    if hindi == largest:
        strong_subjects.append("hindi")


    smallest = physics
    weak_subject = "physics"
    if chemistry<smallest:
        smallest = chemistry
        weak_subject = "chemistry"

    if maths < smallest:
        smallest = maths
        weak_subject = "maths"

    if english < smallest:
        smallest= english
        weak_subject = "english"

    if hindi < smallest :
        smallest= hindi
        weak_subject = "hindi"

    weak_subjects = []

    if physics == smallest:
        weak_subjects.append("physics")

    if chemistry == smallest:
        weak_subjects.append("chemistry")

    if maths == smallest:
        weak_subjects.append("maths")

    if english == smallest:
        weak_subjects.append("english")

    if hindi == smallest:
        weak_subjects.append("hindi")

    if largest == smallest:
        print("\nAll subjects have the same marks.")
        print("There is no single strongest or weakest subject.")

    else:
        
        if len(strong_subjects) == 1:
            print(f"Strongest subject is {strong_subjects[0]} ({largest})")
        else:
            print(f"Strongest subjects are {', '.join(strong_subjects)} ({largest})")
        if len(weak_subjects) == 1:
            print(f"Weakest subject is {weak_subjects[0]} ({smallest})")
        else:
            print(f"Weakest subjects are {', '.join(weak_subjects)} ({smallest})")

    print("\n---------- RECOMMENDATION ----------")
    if largest == smallest:
        print("All subjects have the same marks.")
        print("There is no specific subject that needs more attention.")
    elif smallest < 30:
        print("You have failed in", ", ".join(weak_subjects))
        print("Focus seriously on", ", ".join(weak_subjects))
    elif smallest < 50:
        print("Focus more on", ", ".join(weak_subjects),"to improve your overall performance.")
    elif smallest < 70:
        print("You can improve your performance in:", ", ".join(weak_subjects))
    else:
        print("Good performance! Maintain consistency in all subjects.")

    

print("\n =============CLASS SUMMARY=============== ")

total_percentage=0
passed_students=0
failed_student=0

for student in students:
    total_percentage += student[7]
    if student[8] == "PASS":
        passed_students += 1
    else:
        failed_student += 1
class_average = total_percentage/n
print(f"\nclass_average : {class_average}")
print(f"\npassed_students : {passed_students}")
print(f"\nfailed_students : {failed_student}")


highest_percentage = students[0][7]

for student in students:
    if student[7] > highest_percentage:
        highest_percentage = student[7]

top_students = []

for student in students:
    if student[7] == highest_percentage:
        top_students.append(student[0])

print("\n============= CLASS TOPPER =============")

print(f"Highest Percentage : {highest_percentage:.2f}%")
print("Topper(s) :", ", ".join(top_students))




