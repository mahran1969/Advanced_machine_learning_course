class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        print(f'Name: {self.name}, Age: {self.age}') 
        
        
class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        print(f'Name: {self.name}, Age: {self.age}, Position: {self.position}')
        
        

class Patient(Person):
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        print(f'Medical Record: {self.medical_record}')
        


class Hospital: 
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []
    
    def add_department(self, department):
        self.departments.append(department)



class Department:      
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []
    
    def add_patient(self, patient):
        self.patients.append(patient)
    
    def add_staff(self, staff):
        self.staff.append(staff)
        

# Creating a Hospital
hospital_name = input("Enter the hospital name: ")
hospital_location = input("Enter the hospital location: ")
hospital = Hospital(hospital_name, hospital_location)

# Creating a Department
dept_name = input("Enter the department name: ")
department = Department(dept_name)
hospital.add_department(department)

# Creating a Patient
patient_name = input("Enter patient's name: ")
patient_age = int(input("Enter patient's age: "))
medical_record = input("Enter patient's medical record: ")
patient = Patient(patient_name, patient_age, medical_record)
department.add_patient(patient)

# Creating a Staff member
staff_name = input("Enter staff member's name: ")
staff_age = int(input("Enter staff member's age: "))
position = input("Enter staff member's position: ")
staff = Staff(staff_name, staff_age, position)
department.add_staff(staff)

# Viewing added info
print("\n--- Hospital Information ---")
print(f"Hospital Name: {hospital.name}")
print(f"Location: {hospital.location}")

print("\n--- Department Information ---")
print(f"Department Name: {department.name}")

print("\n--- Patient Information ---")
patient.view_info()
patient.view_record()

print("\n--- Staff Information ---")
staff.view_info()
