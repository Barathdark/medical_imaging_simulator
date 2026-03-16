import random

class HL7Manager:

    def generate_patient_message(self):

        patient_id = random.randint(10000,99999)

        message = f"""
MSH|^~\\&|LAB|HOSPITAL
PID|1||{patient_id}||John Doe
PV1|1|I|Ward
"""

        return message