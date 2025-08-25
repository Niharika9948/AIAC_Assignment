
students = {
    "student1": {"full_name": "Radha", "branch": "CSE", "scgpa": 9},
    "student2": {"full_name": "Krishna", "branch": "ECE", "scgpa": 9.5},
    "student3": {"full_name": "Ravi", "branch": "EEE", "scgpa": 8}
}

def parse_student_info(students_dict):
    """
    Parses a nested dictionary of student information and prints details.
    Each student should have: full_name, branch, scgpa.
    """
    for student_id, info in students_dict.items():
        name = info.get("full_name", "N/A")
        branch = info.get("branch", "N/A")
        scgpa = info.get("scgpa", "N/A")
        print(f"{student_id}: {name}, {branch}, {scgpa}")



# Output
parse_student_info(students)
