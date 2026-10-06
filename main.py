class patient:
    def __init__(self, patient_id, name, age, gender, diagnosis ):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis


    def display_info(self):
        print("/n----------Patient information --------")
        print(f"ID : {self.patient_id}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Diagnosis : {self.diagnosis}")


# hospital class
class hospital: 
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name


        self.patients = []  # List to store patient objects

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient added succesfully.")

    def display_patients(self):
        print(f"/n --------- All patients -----------")
        print(f"/n ------ {self.hospital_name} ------")

        # check if there are any patients in the list
        if len(self.patients) == 0:
            print("No patients found.")
        else:
            for patient in self.patients:
                patient.display_info()


# patient objects
patient1 = patient("P001", "John Doe", 35, "Male", "Poverty")
patient2 = patient("P002", "Jane Smith", 28, "Female", "Allergy")
patient3 = patient("P003", "Michael Johnson", 42, "Male", "Diabetes")   

# hospital object
hospital1 = hospital("City Hospital")

#Adding patients to the hospital
hospital1.add_patient(patient1)
hospital1.add_patient(patient2)
hospital1.add_patient(patient3)

# displaying all patients in the hospital
hospital1.display_patients()