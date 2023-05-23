# Hospital Management System

This is a Hospital Management System implemented in Python. It provides functionalities to manage patients in different specializations within a hospital. The system allows adding new patients, printing patient information, getting the next patient for a specific specialization, and removing patients from the system.

## Table of Contents

**- [Introduction](#introduction)**<br/>
**- [Features](#features)**<br/>
**- [Installation](#installation)**<br/>
**- [Usage](#usage)**<br/>
**- [Contributing](#contributing)**<br/>

## Introduction

The Hospital Management System is designed to help hospital staff efficiently manage patients in different specializations. It provides a user-friendly interface through the command line, allowing staff members to perform various tasks such as adding new patients, viewing patient information, and managing the patient queue.

The system supports three levels of urgency for patients: Normal, Urgent, and Super Urgent. Patients with higher urgency levels are prioritized in the queue. The system also limits the number of patients that can be added to each specialization to ensure efficient management of resources.

## Features

- [x] Add new patients with their name, specialization, and urgency level. <br/>
- [x] Print all patients in the system, grouped by specialization. <br/>
- [x] Get the next patient for a specific specialization. <br/>
- [x] Remove a patient from the system. <br/>
- [x] User-friendly command-line interface. <br/>
- [x] Dummy data generation for testing and demonstration purposes. <br/>

## Installation

1. Clone the repository: <br/>
`git clone https://github.com/AhmedHamdi0/hospital-management-system.git`
2. Navigate to the project directory: <br/>
`cd hospital-management-system`
3. (Optional) Create a virtual environment: <br/>
`python -m venv venv`
4. Activate the virtual environment:
   - For Windows: 
   `venv\Scripts\activate`
   - For Unix or Linux:
    `source venv/bin/activate`
5. Install the required dependencies: <br/>
`pip install -r requirements.txt`

## Usage

To run the Hospital Management System, execute the following command:
`python main.py`

The system will display a menu with options. Enter the corresponding number to perform the desired action.

1. **Add new patient**: Add a new patient to the system by providing the specialization, patient name, and urgency level.
2. **Print all patients**: View all patients in the system, grouped by specialization.
3. **Get next patient**: Get the next patient for a specific specialization.
4. **Remove a leaving patient**: Remove a patient from the system by providing the specialization and patient name.
5. **End the program**: Exit the Hospital Management System.

## Contributing

Contributions to the Hospital Management System are welcome! If you find any issues or want to enhance the system with new features, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`.
3. Make changes and commit them: `git commit -am 'Add new feature'`.
4. Push the branch: `git push origin my-new-feature`.
5. Submit a pull request.