# exception/PatientNumberNotFoundException.py

class PatientNumberNotFoundException(Exception):
    def __init__(self, message="Patient number not found in the database"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"PatientNumberNotFoundException: {self.message}"
