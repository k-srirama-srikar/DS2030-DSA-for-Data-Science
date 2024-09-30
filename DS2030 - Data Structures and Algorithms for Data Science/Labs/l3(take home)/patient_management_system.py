import time
from typing import Optional,Tuple

class Patient:
    # constructor of the class
    def __init__(self, name: str, severity: int, arrival_time: int, condition_type: str) -> None:
        self.name = name
        self.severity = severity
        self.arrival_time = arrival_time
        self.condition_type = condition_type

    # estimate the treatment time
    def get_treatment_time(self) -> int:
        if self.condition_type == "emergency":
            return 5
        elif self.condition_type == "regular":
            return 3
        else:
            return 2
        
    # implementing the comparision method for the priority queue
    def __lt__(self, other: 'Patient') -> bool:
        # this is more like a rank evaluation on the basis of the given conditions
        if self.severity > other.severity:
            return False
        elif self.severity < other.severity:
            return True
        else:
            if self.arrival_time < other.arrival_time:
                return False
            elif self.arrival_time > other.arrival_time:
                return True
            else:
                if self.get_treatment_time() > other.get_treatment_time():
                    return False
                else:
                    return True
                

class Node:
    def __init__(self, patient: 'Patient') -> None:
        self.patient=patient
        self.next=None


class PriorityQueue:
    def __init__(self):
        self.head=None
    
    #checking whether its empty or not
    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False
        
    def insert(self,patient:'Patient')-> None:
        # inserting the patient in the queue
        if self.is_empty() or self.head.patient<patient:
            # if the queue is empty or the patient has max priority ie min rank, 
            # we insert the patient at the beginnig
            n=Node(patient)
            n.next=self.head
            self.head=n
        else:
            n=Node(patient)
            temp=self.head
            # we will traverse through the queue until we find the right place for the new patient
            while temp.next is not None and patient<temp.next.patient:
                temp=temp.next
            n.next=temp.next
            temp.next=n
    def remove(self)->'Patient':
        # to remove a patient we just reassign the head to the next node
        if not self.is_empty():
            temp=self.head
            self.head=self.head.next
            return temp.patient
        # if empty do nothing
        else:
            return None


class Clinic:
    def __init__(self, num_doctors: int) -> None:
        self.num_doctors=num_doctors
        self.doctors=[None]*num_doctors # none implies that the doctor is free
        self.patient_queue=PriorityQueue()
        self.current_time=time.time()

    def add_patient(self,patient:Patient):
        self.patient=patient
        self.patient_queue.insert(patient)

    def treat_patient(self)-> Tuple[Optional[str], Optional[Patient]]:
        
        for i in range(self.num_doctors):
            # while atleast 1 doctor is free. take the first patient from the line and assign him to the doctor
            if self.doctors[i] is None:
                patient=self.patient_queue.remove()
                if patient:
                    self.doctors[i] = patient
                    return f"Doctor {i+1}", patient    
        return (None,None)
        
    def update_doctor_availability(self)-> None:
        self.current_time+=1
        for i in range(self.num_doctors):
            if self.doctors[i]:
                if self.current_time - self.doctors[i].arrival_time >= self.doctors[i].get_treatment_time():
                        self.doctors[i] = None
                else:
                    self.current_time +=1
            
