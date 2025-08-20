class Patient:
    def __init__(self, name, surname, id_number, priority):
        self.name = name
        self.surname = surname
        self.id_number = id_number
        self.priority = priority

    def print_info(self):
        print(f"Name: {self.name}, Surname: {self.surname}, ID: {self.id_number}, Priority: {self.priority}")
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.count = 0

    def add_patient(self, patient):
        heapq.heappush(self.queue, (-patient.priority, self.count, patient))
        self.count += 1

    def get_next_patient(self):
        return heapq.heappop(self.queue)[-1] if self.queue else None

    def print_patients(self):
        for _, _, patient in sorted(self.queue, reverse=True):
            patient.print_info()
class Scheduler:
    def __init__(self):
        self.pq = PriorityQueue()

    def add_patient(self, name, surname, id_number, priority):
        patient = Patient(name, surname, id_number, priority)
        self.pq.add_patient(patient)

    def retrieve_next_patient(self):
        next_patient = self.pq.get_next_patient()
        if next_patient:
            next_patient.print_info()
            return next_patient
        print("No more patients in the queue.")
        return None

    def print_waiting_list(self):
        self.pq.print_patients()

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for _, _, patient in sorted(self.pq.queue, reverse=True):
                file.write(f"{patient.name} {patient.surname} {patient.id_number} {patient.priority}\n")

    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                name, surname, id_number, priority = line.strip().split()
                self.add_patient(name, surname, id_number, int(priority))
def main():
    scheduler = Scheduler()
    while True:
        print("\nMain Menu:")
        print("1. Add Patient")
        print("2. Retrieve Next Patient")
        print("3. Print Waiting List")
        print("4. Save Patient Data to File")
        print("5. Read Patient Data from File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient's name: ")
            surname = input("Enter patient's surname: ")
            id_number = input("Enter patient's ID number: ")
            priority = int(input("Enter priority level (1-5): "))
            scheduler.add_patient(name, surname, id_number, priority)
        elif choice == '2':
            scheduler.retrieve_next_patient()
        elif choice == '3':
            scheduler.print_waiting_list()
        elif choice == '4':
            filename = input("Enter filename to save to: ")
            scheduler.save_to_file(filename)
        elif choice == '5':
            filename = input("Enter filename to read from: ")
            scheduler.read_from_file(filename)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, pl ease try again.")

if __name__ == "__main__":
    main()
