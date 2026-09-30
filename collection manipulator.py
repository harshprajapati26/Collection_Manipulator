# ==========================================
# PROJECT: COLLECTION MANIPULATOR
# Student Data Organizer
# ==========================================

# List to store all students
students = []
print("\n============================================================")
print("WELCOME TO COLLECTION MANIPULATOR PROGRAM BY HARSH PRAJAPATI")
print("============================================================")

while True:

    print("\n================================")
    print("     STUDENT DATA ORGANIZER")
    print("================================")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")


    # --------------------------------
    # 1. ADD STUDENT
    # --------------------------------

    if choice == "1":

        print("\nEnter Student Details")

        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth: ")

        subjects = input("Enter subjects : ")

        # Convert subjects into a set
        subjects = set(subjects.split(","))

        # Tuple
        # ID and Date of Birth are stored together
        id_dob = (student_id, dob)

        # Dictionary
        student = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        # Add dictionary to the list
        students.append(student)

        print("Student added successfully!")


    # --------------------------------
    # 2. DISPLAY ALL STUDENTS
    # --------------------------------

    elif choice == "2":

        if len(students) == 0:

            print("\nNo student records found.")

        else:

            print("\n========== ALL STUDENTS ==========")

            for student in students:

                print("\nStudent ID:", student["id_dob"][0])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Grade:", student["grade"])
                print("Date of Birth:", student["id_dob"][1])
                print("Subjects:", student["subjects"])


    # --------------------------------
    # 3. UPDATE STUDENT
    # --------------------------------

    elif choice == "3":

        student_id = int(input("\nEnter Student ID to update: "))

        found = False

        for student in students:

            if student["id_dob"][0] == student_id:

                print("\nWhat do you want to update?")
                print("1. Age")
                print("2. Grade")
                print("3. Subjects")

                option = input("Enter your choice: ")

                if option == "1":

                    new_age = int(input("Enter new age: "))

                    student["age"] = new_age

                    print("Age updated successfully!")


                elif option == "2":

                    new_grade = input("Enter new grade: ")

                    student["grade"] = new_grade

                    print("Grade updated successfully!")


                elif option == "3":

                    new_subjects = input(
                        "Enter new subjects : "
                    )

                    student["subjects"] = set(
                        new_subjects.split(",")
                    )

                    print("Subjects updated successfully!")


                else:

                    print("Invalid choice.")

                found = True
                break


        if found == False:

            print("Student not found.")


    # --------------------------------
    # 4. DELETE STUDENT
    # --------------------------------

    elif choice == "4":

        student_id = int(input("\nEnter Student ID to delete: "))

        found = False

        for i in range(len(students)):

            if students[i]["id_dob"][0] == student_id:

                # Delete student using del
                del students[i]

                print("Student deleted successfully!")

                found = True
                break


        if found == False:

            print("Student not found.")


    # --------------------------------
    # 5. DISPLAY SUBJECTS
    # --------------------------------

    elif choice == "5":

        all_subjects = set()

        for student in students:

            all_subjects.update(student["subjects"])


        print("\n========== SUBJECTS OFFERED ==========")

        if len(all_subjects) == 0:

            print("No subjects found.")

        else:

            for subject in all_subjects:

                print("-", subject)


    # --------------------------------
    # 6. EXIT
    # --------------------------------

    elif choice == "6":

        print("\nThank you for using Student Data Organizer!")

        print("Program ended.")

        break


    # --------------------------------
    # INVALID CHOICE
    # --------------------------------

    else:

        print("\nInvalid choice!")
        print("Please enter a number from 1 to 6.")
