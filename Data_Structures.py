# Program to store student data and perform CRUD operations
def student_data_operations():
    students = {}
# Add Operation
    def add_student(name, age, division):
        students[name] = {"age": age, "division": division}
        print(f"Student '{name}' added successfully.")
# Update Operation
    def update_student(name, age=None, division=None):
        if name in students:
            if age: students[name]['age'] = age
            if division: students[name]['division'] = division
            print(f"Student '{name}' updated successfully.")
        else:
            print(f"Student '{name}' not found.")
# Delete Operation
    def delete_student(name):
        if name in students:
            del students[name]
            print(f"Student '{name}' deleted successfully.")
        else:
            print(f"Student '{name}' not found.")
#
    def display_students():
        for name, details in students.items():
            print(f"Name: {name}, Age: {details['age']}, Division: {details['division']}")

    # Example operations
    add_student("Sonia", 20, "TE-A")
    add_student("Sanjana", 22, "TE-B")
    display_students()
    update_student("Sonia", division="BE-A")
    delete_student("Sanjana")
    display_students()

student_data_operations()
