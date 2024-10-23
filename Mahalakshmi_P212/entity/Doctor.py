# entity/Doctor.py
class Doctor:
    def __init__(self, doctorId, firstName, lastName, specialization, contactNumber):
        self.doctorId = doctorId
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.contactNumber = contactNumber

    # Getters and Setters
    def get_doctorId(self):
        return self.doctorId

    def set_doctorId(self, doctorId):
        self.doctorId = doctorId

    def get_firstName(self):
        return self.firstName

    def set_firstName(self, firstName):
        self.firstName = firstName

    def get_lastName(self):
        return self.lastName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, specialization):
        self.specialization = specialization

    def get_contactNumber(self):
        return self.contactNumber

    def set_contactNumber(self, contactNumber):
        self.contactNumber = contactNumber

    # __str__ method to print doctor details
    def __str__(self):
        return f"Doctor[ID: {self.doctorId}, Name: {self.firstName} {self.lastName}, Specialization: {self.specialization}, Contact: {self.contactNumber}]"
