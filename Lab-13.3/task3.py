class Student:
    """
    Represents a student with a name, age, and a list of marks.
    Provides methods to display details and calculate total marks.
    """
    def __init__(self, name, age, mark1, mark2, mark3):
        """
        Initialize a Student instance.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            mark1 (int or float): The first mark.
            mark2 (int or float): The second mark.
            mark3 (int or float): The third mark.
        """
        self.name = name
        self.age = age
        self.marks = [mark1, mark2, mark3]

    def details(self):
        """
        Prints the student's name and age in a readable format.
        """
        print(f"Name: {self.name}\nAge: {self.age}")

    def total(self):
        """
        Returns the total of the student's marks.

        Returns:
            int or float: The sum of the marks.
        """
        return sum(self.marks)

# Example usage and output
student = Student("Alice", 20, 85, 90, 95)
student.details()
print("Total Marks:", student.total())

