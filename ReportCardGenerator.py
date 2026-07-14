
"""
Student Report Card Generator
------------------------------
Takes student ID, name, and marks for multiple subjects,
stores them in a dictionary, calculates average and grade,
then prints a formatted report card for each student.
"""
 
 
def get_grade(average):
    """Return a letter grade based on the average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"
 
 
def get_subject_marks():
    """Prompt the user for subject names and marks, return as a dict."""
    subjects = {}
    try:
        num_subjects = int(input("How many subjects? "))
    except ValueError:
        print("Please enter a valid number. Defaulting to 0 subjects.")
        return subjects
 
    for i in range(num_subjects):
        subject = input(f"  Subject {i + 1} name: ").strip()
        while True:
            try:
                marks = float(input(f"  Marks for {subject} (0-100): "))
                if 0 <= marks <= 100:
                    break
                print("  Marks must be between 0 and 100.")
            except ValueError:
                print("  Please enter a valid number.")
        subjects[subject] = marks
    return subjects
 
 
def collect_students():
    """Collect data for multiple students and return a list of student dicts."""
    students = []
    try:
        num_students = int(input("How many students? "))
    except ValueError:
        print("Please enter a valid number. Defaulting to 0 students.")
        return students
 
    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        student_id = input("Student ID: ").strip()
        name = input("Student Name: ").strip()
        subjects = get_subject_marks()
 
        total = sum(subjects.values())
        average = total / len(subjects) if subjects else 0
        grade = get_grade(average)
 
        students.append({
            "id": student_id,
            "name": name,
            "subjects": subjects,
            "total": total,
            "average": average,
            "grade": grade,
        })
 
    return students
 
 
def print_report_card(student):
    """Print a nicely formatted report card for a single student."""
    width = 40
    print("\n" + "=" * width)
    print("STUDENT REPORT CARD".center(width))
    print("=" * width)
    print(f"Student ID : {student['id']}")
    print(f"Name       : {student['name']}")
    print("-" * width)
    print(f"{'Subject':<20}{'Marks':>10}")
    print("-" * width)
    for subject, marks in student["subjects"].items():
        print(f"{subject:<20}{marks:>10.2f}")
    print("-" * width)
    print(f"{'Total':<20}{student['total']:>10.2f}")
    print(f"{'Average':<20}{student['average']:>10.2f}")
    print(f"{'Grade':<20}{student['grade']:>10}")
    print("=" * width)
 
 
def main():
    print("Welcome to the Student Report Card Generator!\n")
    students = collect_students()
 
    print("\n\nGenerating Report Cards...")
    for student in students:
        print_report_card(student)
 
 
if __name__ == "__main__":
    main()
 
