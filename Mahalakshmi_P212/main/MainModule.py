# main/MainModule.py

from dao.HospitalServiceImpl import HospitalServiceImpl
from entity.Appointment import Appointment
from exception.PatientNumberNotFoundException import PatientNumberNotFoundException
from datetime import datetime


def main():
    service = HospitalServiceImpl()

    while True:
        print("\n===== Hospital Management System =====")
        print("1. View Appointment by Appointment ID")
        print("2. View All Appointments for a Patient")
        print("3. View All Appointments for a Doctor")
        print("4. Schedule an Appointment")
        print("5. Update an Appointment")
        print("6. Cancel an Appointment")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            appointment_id = input("Enter appointment ID: ")
            appointment = service.get_appointment_by_id(appointment_id)
            if appointment:
                print(f"Appointment Details: {appointment}")
            else:
                print("No appointment found with that ID.")

        elif choice == '2':
            patient_id = input("Enter patient ID: ")
            try:
                appointments = service.get_appointments_for_patient(patient_id)
                if not appointments:
                    raise PatientNumberNotFoundException(f"No appointments found for patient with ID {patient_id}.")
                for appointment in appointments:
                    print(appointment)
            except PatientNumberNotFoundException as e:
                print(e)

        elif choice == '3':
            doctor_id = input("Enter doctor ID: ")
            appointments = service.get_appointments_for_doctor(doctor_id)
            if not appointments:
                print(f"No appointments found for doctor with ID {doctor_id}.")
            else:
                for appointment in appointments:
                    print(appointment)

        elif choice == '4':
            appointment_id = input("Enter new appointment ID: ")
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            appointment_date = input("Enter appointment date (YYYY-MM-DD HH:MM:SS): ")
            description = input("Enter appointment description: ")

            # Create appointment object
            appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)
            if service.schedule_appointment(appointment):
                print("Appointment scheduled successfully.")
            else:
                print("Failed to schedule appointment.")

        elif choice == '5':
            appointment_id = input("Enter appointment ID to update: ")
            patient_id = input("Enter updated patient ID: ")
            doctor_id = input("Enter updated doctor ID: ")
            appointment_date = input("Enter updated appointment date (YYYY-MM-DD HH:MM:SS): ")
            description = input("Enter updated appointment description: ")

            # Create updated appointment object
            appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)
            if service.update_appointment(appointment):
                print("Appointment updated successfully.")
            else:
                print("Failed to update appointment.")

        elif choice == '6':
            appointment_id = input("Enter appointment ID to cancel: ")
            if service.cancel_appointment(appointment_id):
                print("Appointment canceled successfully.")
            else:
                print("Failed to cancel appointment.")

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
