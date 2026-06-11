name = input("Enter your name : ")
marks = []
n = int(input("Enter no. of subjects you have : "))
subjects = []
for i in range(1,n+1):
    subjects.append(input(f"Enter name of subject {i} : "))
print()

for i in range(1,n+1):
    marks.append(int(input(f"Enter marks of subject {i} : ")))

student_analyzer = dict(zip(subjects,marks))
# print(student_analyzer)

total = sum(marks)
avg = total/n

def calculate_grade(avg):
    if avg >= 75:
        grade = 'A'
    elif avg < 74 and avg >= 60:
        grade = 'B'
    elif avg < 59 and avg >= 40:
        grade = 'C'
    else:
        grade = 'D'

    return grade


def is_passed(marks):
    
    passed = True
    for mark in marks:
        if mark < 40:
            passed = False
            break 

    return passed

def generate_remark(avg, is_passed):
    if not is_passed:
        remark = "Needs improvement. Identify weak subjects, seek guidance, and follow a structured study plan."

    elif avg >= 75:
        remark = "Excellent performance! Keep up the consistent study routine and aim for excellence."

    elif avg >= 60:
        remark = "Good performance. Focus more on weaker subjects and practice regularly to improve your grades."

    elif avg >= 40:
        remark = "Average result. You should increase daily study time and revise concepts regularly."

    else:
        remark = "Needs improvement. Significant effort is required to clear the subjects."

    return remark


def analyze_subjects(student_analyzer):
    analysis = {}

    for subject, mark in student_analyzer.items():
        if mark >= 75:
            analysis[subject] = "Strong"
        elif mark >= 60:
            analysis[subject] = "Good"
        elif mark >= 40:
            analysis[subject] = "Average"
        else:
            analysis[subject] = "Weak"

    return analysis

strong_subject = max(student_analyzer, key=student_analyzer.get)
weak_subject = min(student_analyzer, key=student_analyzer.get)


grade = calculate_grade(avg)
passed = is_passed(marks)
remark = generate_remark(avg, passed)

print()
print("STUDENT INFORMATION : ")
print(f"Name : {name}")
print(f"Total Marks : {total}")
print(f"Average Marks : {avg}")
print(f"Grade : {grade}")
print()

subject_analysis = analyze_subjects(student_analyzer)
print("STUDENT PERFORMANCE : ")
print("Subject-wise Analysis:")
for subject, status in subject_analysis.items():
    print(f"{subject} : {status}")
print()

print(f"Strongest Subject : {strong_subject}")
print(f"Weakest Subject : {weak_subject}")
print()

print(f"Remark : {remark}")