"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_details = get_data()
    print_subjects(subject_details)
    print("END OF PROGRAM")


def print_subjects(subject_details):
    """Display subject, lecturer name, number of students"""
    for subject_detail in subject_details:
        print(f"{subject_detail[0]} is taught by {subject_detail[1]:12} and has {subject_detail[2]:3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_detail = [parts[0], parts[1], parts[2]]
        subject_details.append(subject_detail)
    input_file.close()
    return subject_details


main()
