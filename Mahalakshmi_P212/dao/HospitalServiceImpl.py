# dao/HospitalServiceImpl.py

from dao.IHospitalService import IHospitalService
from util.DBConnUtil import DBConnUtil
from entity.Appointment import Appointment
from entity.Patient import Patient
from entity.Doctor import Doctor

class HospitalServiceImpl(IHospitalService):

    def get_appointment_by_id(self, appointmentId):
        """Fetch appointment by appointmentId"""
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Appointment WHERE appointmentId = ?"
        cursor.execute(query, appointmentId)
        row = cursor.fetchone()

        if row:
            appointment = Appointment(row[0], row[1], row[2], row[3], row[4])
            return appointment
        return None

    def get_appointments_for_patient(self, patientId):
        """Fetch all appointments for a given patient"""
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Appointment WHERE patientId = ?"
        cursor.execute(query, patientId)
        rows = cursor.fetchall()

        appointments = []
        for row in rows:
            appointment = Appointment(row[0], row[1], row[2], row[3], row[4])
            appointments.append(appointment)
        return appointments

    def get_appointments_for_doctor(self, doctorId):
        """Fetch all appointments for a given doctor"""
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Appointment WHERE doctorId = ?"
        cursor.execute(query, doctorId)
        rows = cursor.fetchall()

        appointments = []
        for row in rows:
            appointment = Appointment(row[0], row[1], row[2], row[3], row[4])
            appointments.append(appointment)
        return appointments

    def schedule_appointment(self, appointment):
        """Schedule a new appointment"""
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Appointment (appointmentId, patientId, doctorId, appointmentDate, description)
                   VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, (appointment.appointmentId, appointment.patientId, appointment.doctorId,
                               appointment.appointmentDate, appointment.description))
        conn.commit()
        return True

    def update_appointment(self, appointment):
        """Update an existing appointment"""
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """UPDATE Appointment
                   SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ?
                   WHERE appointmentId = ?"""
        cursor.execute(query, (appointment.patientId, appointment.doctorId, appointment.appointmentDate,
                               appointment.description, appointment.appointmentId))
        conn.commit()
        return True

    def cancel_appointment(self, appointmentId):
        """Cancel an appointment by appointmentId"""
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Appointment WHERE appointmentId = ?"
        cursor.execute(query, appointmentId)
        conn.commit()
        return True
