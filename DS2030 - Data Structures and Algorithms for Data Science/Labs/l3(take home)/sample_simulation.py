import time
from patient_management_system import *

clinic = Clinic ( num_doctors =3)

patients = [
    Patient ( "Aarav" , 5 , time.time () , "regular" ) ,
    Patient ( "Isha" , 7 , time.time () + 1 , "emergency" ) ,
    Patient ( "Ravi" , 6 , time.time () + 2 , "follow - up" ) ,
    Patient ( "Meera" , 4 , time.time () + 3 , "regular" ) ,
    Patient ( "Aditya" , 8 , time.time () + 4 , "emergency" ) ,
    ]

for patient in patients :
    clinic.add_patient(patient)

time_unit = 1
while time_unit <= 10:
    print(f"\nTime unit {time_unit}: ")
    clinic.update_doctor_availability()
    doctor, patient = clinic.treat_patient()
    if doctor and patient :
        print (f"{doctor} is treating {patient.name} for {patient.condition_type}. " )
    time_unit += 1
    time.sleep (1)