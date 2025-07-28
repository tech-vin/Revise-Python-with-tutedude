# Task 1: Create a Dictionary of Student Marks
FILE_PATH='files/student_data.txt'
# students_dict = {
#     'Alice': 35,
#     'John': 65,
#     'Emma': 91,
#     'Chris': 82
# }

def addDetails(name, marks):
    with open(FILE_PATH, 'a') as file:
        file.write(f'{name}:{marks}\n')

def fetchDetails():
    students_dict = {}
    with open(FILE_PATH, 'r') as file:
        for line in file:
            if ':' in line:
                name, marks = line.strip().split(':')
                students_dict[name.strip()] = int(marks.strip())
    return students_dict


while True:
    msg='''
    1. Add Details
    2. Fetch Details
    3. Exit
    '''
    print(msg)
    choice = int(input('Enter Choice: '))
    if choice == 3:
        print("Exiting the loop...")
        break

    elif choice == 1:
        print('*'* 5 + 'ADD DETAILS' + '*'* 5)
        detail = input("Format (name=marks): ")
        try:
            name, marks = detail.split("=")
            marks = int(marks)
            addDetails(name.strip(), marks)
            print(f'{name.strip()} added with marks: {marks}.')
        except Exception as ep:
            print('Invalid Input!')

    elif choice == 2:
        name = input('Enter the student\'s name: ').strip()
        student_dict = fetchDetails()
        if name in student_dict:
            print('-'*25)
            print('{}\'s marks: {}'.format(name, student_dict[name]))
            print('-'*25)
        else:
            print('-'*25)
            print('Student not found!')
            print('-'*25)
    else:
        print("Invalid choice, valid range (1,2,3).")
    