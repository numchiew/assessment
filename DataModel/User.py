from datetime import datetime


class User:

    def __init__(self, id, first_name, last_name, dob, address, contact_number, created_time, modified_time):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.strftime(dob, '%d-%m-%Y')
        self.address = address
        self.contact_number = contact_number
        self.created_time = created_time
        self.modified_time = modified_time

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.get_full_name()} Date of Birth {self.dob} Contact Information {self.contact_number} {self.address} "
