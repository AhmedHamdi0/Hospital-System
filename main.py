def validate_input(msg, start=0, end=None):
    # keep iterating till the given input is valid
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
            else:
                return int(inp)
        else:
            return int(inp)


class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        status = ['Normal', 'Urgent', 'Super Urgent'][self.status]
        return f'Patient: {self.name} is {status}'

    def __repr__(self):
        return F'Patient(name="{self.name}", status={self.status})'

    def __lt__(self, other):
        return self.status > other.status


class HospitalManger:
    def __init__(self, specializations_count):
        self.specializations = [[] for one_specialization in range(specializations_count)]
        self.MAX_QUEUE = 10
        self.NORMAL = 0
        self.URGENT = 1
        self.SUPER_URGENT = 2

    def can_add_more_patients(self, specialization):
        return len(self.specializations[specialization]) < self.MAX_QUEUE

    def add_patient_smart(self, specialization, name, status):
        spec = self.specializations[specialization]
        spec.append(Patient(name, status))
        spec.sort()

    def add_patient(self, specialization, name, status):
        spec = self.specializations[specialization]
        pat = Patient(name, status)

        if status == 0 or len(spec) == 0:  # Add normal
            spec.append(pat)  # Add at end
        elif status == 1:  # Add urgent
            # Add before the normal patients, but after current urgent / super-urgent
            if spec[-1].status != self.NORMAL:  # if no normals, then it should be added after the end
                spec.append(pat)
            else:  # Find the first normal and add before it
                for idx, patient in enumerate(spec):
                    if patient.status == self.NORMAL:
                        spec.insert(idx, pat)
                        break
        else:
            # Add before the normal or urgent patients, but after current super-urgent
            if spec[-1].status == self.SUPER_URGENT:  # if all are super urgent, just add at the end
                spec.append(pat)
            else:  # Find the first normal/urgent and add before it
                for idx, patient in enumerate(spec):
                    if patient.status == self.NORMAL or patient.status == self.URGENT:
                        spec.insert(idx, pat)
                        break

    def get_printable_patients_info(self):
        all_patients = []  # send back results to front end to print on its way
        for idx, specialization in enumerate(self.specializations):
            if not specialization:
                continue
            current_patients = []
            for patient in specialization:
                current_patients.append(str(patient))
            all_patients.append((idx, current_patients))
        return all_patients

    def get_next_patients(self, specialization):
        if len(self.specializations[specialization]) == 0:
            return None
        return self.specializations[specialization].pop(0)

    def remove_patient(self, specialization, name):
        spec = self.specializations[specialization]
        for idx, patient in enumerate(spec):
            if patient.name == name:
                del spec[idx]
                return True
        return False


class FrontendManager:
    def __init__(self, specializations_count=20):
        self.specializations_count = specializations_count
        self.hospital_manger = HospitalManger(self.specializations_count)
        self.add_dummy_data()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            'Add new patient',
            'Print all patients',
            'Get next patient',
            'Remove a leaving patient',
            'End the program'
        ]
        messages = [f'{idx+1}) {msg}' for idx, msg in enumerate(messages)]
        print('\n'.join(messages))
        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return validate_input(msg, 1, len(messages))

    def add_dummy_data(self):
        for i in range(10):
            self.hospital_manger.add_patient(2, 'Dummy' + str(i), i % 3)
        for i in range(4):
            self.hospital_manger.add_patient(5, 'AnotherDummy' + str(i), 0)
        for i in range(5):
            self.hospital_manger.add_patient(8, 'ThirdDummy' + str(i), 1)
        for i in range(3):
            self.hospital_manger.add_patient(12, 'ForthDummy' + str(i), 2)
        for i in range(3):
            self.hospital_manger.add_patient(13, 'FifthDummy' + str(i), 1)
            self.hospital_manger.add_patient(13, 'FifthDummy' + str(i + 5), 2)

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                specialization = validate_input('Enter specialization: ', 1, self.specializations_count) - 1

                if self.hospital_manger.can_add_more_patients(specialization):
                    name = input('Enter patient name: ')
                    status = validate_input('Enter status (0 normal / 1 urgent / 2 super urgent): ', 0, 2)
                    self.hospital_manger.add_patient(specialization, name, status)
                else:
                    print("Sorry we can't add more patients for this specialization at the moment.")
            elif choice == 2:
                all_patients = self.hospital_manger.get_printable_patients_info()
                if not all_patients:
                    print('No patients at the moment')
                else:
                    for idx, patients_info in all_patients:
                        print(f'Specialization {idx + 1}: There are {len(patients_info)} patients.')
                        print("\n".join(patients_info) + '\n')
            elif choice == 3:
                specialization = validate_input('Enter specialization: ', 1, self.specializations_count) - 1
                patient = self.hospital_manger.get_next_patients(specialization)

                if patient is None:
                    print('No patients at the moment. Have rest, Dr')
                else:
                    print(f'{patient.name}, Please go with the Dr')
            elif choice == 4:
                specialization = validate_input('Enter specialization: ', 1, self.specializations_count) - 1
                name = input('Enter patient name: ')
                if not self.hospital_manger.remove_patient(specialization, name):
                    print('No patient with such a name in this specialization!')
            else:
                break


if __name__ == '__main__':
    app = FrontendManager()
    app.run()