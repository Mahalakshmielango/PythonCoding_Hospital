# dao/IHospitalService.py

from abc import ABC, abstractmethod

class IHospitalService(ABC):
    @abstractmethod
    def get_appointment_by_id(self, appointmentId):
        """Fetch appointment by appointmentId"""
        pass

    @abstractmethod
    def get_appointments_for_patient(self, patientId):
        """Fetch all appointments for a given patient by patientId"""
        pass

    @abstractmethod
    def get_appointments_for_doctor(self, doctorId):
        """Fetch all appointments for a given doctor by doctorId"""
        pass

    @abstractmethod
    def schedule_appointment(self, appointment):
        """Schedule a new appointment"""
        pass

    @abstractmethod
    def update_appointment(self, appointment):
        """Update an existing appointment"""
        pass

    @abstractmethod
    def cancel_appointment(self, appointmentId):
        """Cancel an appointment by appointmentId"""
        pass
