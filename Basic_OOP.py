# Student class with attributes and methods
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

# Example usage
student = Student("Sonia", 20, [88, 90, 92])
student.display_details()
print("Average Grade:", student.calculate_average())
