# ============================================================
#        SMART CAMPUS INFORMATION SYSTEM
# ============================================================

import os


# ============================================================
#  LAB 1 - Student Registration & Grade Evaluation
# ============================================================

def get_grade(score):
    if 90 <= score <= 100:
        return "A", "Excellent"
    elif score >= 75:
        return "B", "Very Good"
    elif score >= 60:
        return "C", "Good"
    elif score >= 40:
        return "D", "Average"
    else:
        return "F", "Needs Improvement"


def student_registration():
    print("\n" + "=" * 45)
    print("   MODULE 1 : Student Registration & Grade")
    print("=" * 45)

    name = input("  Enter student name : ").strip()
    if not name:
        print("  [!] Name cannot be empty.")
        return

    try:
        score = float(input("  Enter exam score (0-100) : "))
    except ValueError:
        print("  [!] Invalid score. Please enter a number.")
        return

    if not (0 <= score <= 100):
        print("  [!] Score must be between 0 and 100.")
        return

    grade, remark = get_grade(score)

    print("\n  --- Student Report ---")
    print(f"  Name        : {name}")
    print(f"  Score       : {score}")
    print(f"  Grade       : {grade}")
    print(f"  Performance : {remark}")


# ============================================================
#  LAB 2 - Course Enrollment Management
# ============================================================

def course_enrollment():
    print("\n" + "=" * 45)
    print("   MODULE 2 : Course Enrollment Management")
    print("=" * 45)

    MAX_COURSES  = 5
    local_courses = []   # fresh list every time this module runs

    while True:
        if len(local_courses) >= MAX_COURSES:
            print(f"  [!] Maximum course limit ({MAX_COURSES}) reached!")
            break

        course_name = input("\n  Enter course name (or 'done' to finish) : ").strip()
        if course_name.lower() == "done":
            break
        if not course_name:
            print("  [!] Course name cannot be empty. Skipping...")
            continue

        credits_input = input("  Enter credit value : ").strip()
        if not credits_input.isdigit():
            print("  [!] Invalid credit value! Skipping entry...")
            continue

        credits = int(credits_input)
        if credits <= 0:
            print("  [!] Credit must be positive! Skipping entry...")
            continue

        local_courses.append((course_name, credits))
        print(f"  [[OK]] Course '{course_name}' with {credits} credit(s) added.")

    print("\n  --- Enrollment Report ---")
    if not local_courses:
        print("  No courses enrolled.")
    else:
        for course, credit in local_courses:
            print(f"  Course : {course:<25}  Credits : {credit}")
        print(f"  Total courses enrolled : {len(local_courses)}")


# ============================================================
#  LAB 3 - Student Record Data Management
# ============================================================

def student_records():
    print("\n" + "=" * 45)
    print("   MODULE 3 : Student Record Management")
    print("=" * 45)

    local_students = []   # fresh list, independent of other modules

    sub_menu = """
  1. Add student record
  2. View all student records
  3. Event participation analysis
  0. Back to main menu
  Choice : """

    while True:
        choice = input(sub_menu).strip()

        if choice == "1":
            name = input("  Enter student name : ").strip()
            if not name:
                print("  [!] Name cannot be empty.")
                continue

            try:
                age = int(input("  Enter age : "))
            except ValueError:
                print("  [!] Invalid age.")
                continue

            grades_input = input("  Enter grades separated by commas : ").strip()
            try:
                grades = [float(g.strip()) for g in grades_input.split(",")]
            except ValueError:
                print("  [!] Invalid grades input.")
                continue

            local_students.append({"name": name, "age": age, "grades": grades})
            print(f"  [[OK]] Record for '{name}' added.")

        elif choice == "2":
            if not local_students:
                print("  No records found. Add records first.")
            else:
                print("\n  === Student Records ===")
                for s in local_students:
                    print(f"  Name   : {s['name']}")
                    print(f"  Age    : {s['age']}")
                    print(f"  Grades : {s['grades']}")
                    print("  " + "-" * 30)

        elif choice == "3":
            print("\n  --- Event Participation Analysis ---")
            event_a_input = input("  Enter Event A participants (comma-separated) : ")
            event_b_input = input("  Enter Event B participants (comma-separated) : ")

            event_A = {n.strip() for n in event_a_input.split(",") if n.strip()}
            event_B = {n.strip() for n in event_b_input.split(",") if n.strip()}

            print(f"\n  Common Participants  : {event_A & event_B}")
            print(f"  All Participants     : {event_A | event_B}")
            print(f"  Only in Event A      : {event_A - event_B}")
            print(f"  Only in Event B      : {event_B - event_A}")

        elif choice == "0":
            break
        else:
            print("  [!] Invalid choice.")


# ============================================================
#  LAB 4 - Sorting & Searching Student IDs
# ============================================================

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def sort_search():
    print("\n" + "=" * 45)
    print("   MODULE 4 : Sort & Search Student IDs")
    print("=" * 45)

    local_ids = []   # fresh list, independent of other modules

    sub_menu = """
  1. Add student IDs
  2. View current IDs
  3. Sort IDs (Bubble Sort)
  4. Sort IDs (Selection Sort)
  5. Linear Search
  6. Binary Search
  0. Back to main menu
  Choice : """

    while True:
        choice = input(sub_menu).strip()

        if choice == "1":
            raw = input("  Enter student IDs separated by commas : ").strip()
            try:
                new_ids = [int(x.strip()) for x in raw.split(",")]
                local_ids.extend(new_ids)
                print(f"  [[OK]] Added IDs : {new_ids}")
            except ValueError:
                print("  [!] Invalid input. Enter integers only.")

        elif choice == "2":
            print(f"  Current IDs : {local_ids}")

        elif choice == "3":
            if not local_ids:
                print("  [!] No IDs available. Add IDs first.")
            else:
                print(f"  Sorted (Bubble Sort)    : {bubble_sort(local_ids)}")

        elif choice == "4":
            if not local_ids:
                print("  [!] No IDs available. Add IDs first.")
            else:
                print(f"  Sorted (Selection Sort) : {selection_sort(local_ids)}")

        elif choice == "5":
            if not local_ids:
                print("  [!] No IDs available. Add IDs first.")
            else:
                try:
                    target = int(input("  Enter ID to search : "))
                    idx = linear_search(local_ids, target)
                    if idx != -1:
                        print(f"  [[OK]] Linear Search : ID {target} found at index {idx}.")
                    else:
                        print(f"  [[X]] Linear Search : ID {target} not found.")
                except ValueError:
                    print("  [!] Invalid ID.")

        elif choice == "6":
            if not local_ids:
                print("  [!] No IDs available. Add IDs first.")
            else:
                try:
                    target = int(input("  Enter ID to search : "))
                    sorted_ids = bubble_sort(local_ids)
                    idx = binary_search(sorted_ids, target)
                    if idx != -1:
                        print(f"  [[OK]] Binary Search : ID {target} found at index {idx} (in sorted list).")
                    else:
                        print(f"  [[X]] Binary Search : ID {target} not found.")
                except ValueError:
                    print("  [!] Invalid ID.")

        elif choice == "0":
            break
        else:
            print("  [!] Invalid choice.")


# ============================================================
#  LAB 5 - Student Fee Calculation using Functions
# ============================================================

def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    return tuition_fee + hostel_fee + transportation_fee


def fee_calculation():
    print("\n" + "=" * 45)
    print("   MODULE 5 : Student Fee Calculation")
    print("=" * 45)

    try:
        tuition = float(input("  Enter tuition fee (Rs.) : "))

        hostel_input = input("  Enter hostel fee (Rs.) [press Enter to skip] : ").strip()
        hostel = float(hostel_input) if hostel_input else 0

        transport_input = input("  Enter transportation fee (Rs.) [press Enter to skip] : ").strip()
        transport = float(transport_input) if transport_input else 0

    except ValueError:
        print("  [!] Invalid amount entered.")
        return

    total = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)

    print("\n  --- Fee Breakdown ---")
    print(f"  Tuition Fee        : Rs. {tuition:,.2f}")
    print(f"  Hostel Fee         : Rs. {hostel:,.2f}")
    print(f"  Transportation Fee : Rs. {transport:,.2f}")
    print(f"  {'-' * 32}")
    print(f"  Total Fee          : Rs. {total:,.2f}")


# ============================================================
#  LAB 6 - File Handling for Academic Records
# ============================================================

FILE_NAME = "student_records.txt"


def lab6_write_records():
    print("\n  --- Write Student Records to File ---")
    local_records = []
    print("  Enter student details (type 'done' as name to stop)\n")

    sid = 101
    while True:
        name = input(f"  Enter name for student ID {sid} : ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("  [!] Name cannot be empty. Try again.")
            continue

        try:
            marks = float(input(f"  Enter marks for {name} : "))
        except ValueError:
            print("  [!] Invalid marks. Skipping...")
            continue

        local_records.append((sid, name, marks))
        sid += 1

    if not local_records:
        print("  [!] No records to write.")
        return

    try:
        with open(FILE_NAME, "w") as f:
            f.write("ID,Name,Marks\n")
            for sid, name, marks in local_records:
                f.write(f"{sid},{name},{marks}\n")
        print(f"  [[OK]] {len(local_records)} record(s) written to '{FILE_NAME}'.")
    except Exception as e:
        print(f"  [!] Error writing file : {e}")


def lab6_read_records():
    print("\n  --- Read Records from File ---")
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
        if not lines:
            print("  [!] File is empty.")
            return []
        print(f"\n  Contents of '{FILE_NAME}' :")
        for line in lines:
            print("   ", line.strip())
        return lines
    except FileNotFoundError:
        print(f"  [!] File '{FILE_NAME}' not found. Write records first.")
        return []
    except Exception as e:
        print(f"  [!] Error : {e}")
        return []


def lab6_generate_report(records):
    print("\n  --- Performance Report ---")
    if len(records) <= 1:
        print("  [!] No student data in file.")
        return

    total_students = 0
    total_marks    = 0.0
    highest_marks  = -1
    top_student    = ""

    for record in records[1:]:
        parts = record.strip().split(",")
        if len(parts) < 3:
            continue
        try:
            marks = float(parts[2])
        except ValueError:
            continue
        name = parts[1]
        total_students += 1
        total_marks    += marks
        if marks > highest_marks:
            highest_marks = marks
            top_student   = name

    if total_students == 0:
        print("  [!] No valid records found.")
        return

    print(f"  Total Students : {total_students}")
    print(f"  Average Marks  : {total_marks / total_students:.2f}")
    print(f"  Top Student    : {top_student}  ({highest_marks} marks)")


def file_management():
    print("\n" + "=" * 45)
    print("   MODULE 6 : File Handling - Academic Records")
    print("=" * 45)

    sub_menu = """
  1. Write student records to file
  2. Read records from file
  3. Generate performance report
  0. Back to main menu
  Choice : """

    while True:
        choice = input(sub_menu).strip()

        if choice == "1":
            lab6_write_records()

        elif choice == "2":
            lab6_read_records()

        elif choice == "3":
            records = lab6_read_records()
            if records:
                lab6_generate_report(records)

        elif choice == "0":
            break
        else:
            print("  [!] Invalid choice.")


# ============================================================
#  LAB 7 - Directory Scanning with Exception Handling
# ============================================================

class MissingFileOrFolderError(Exception):
    pass


def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: '{path}'")

        if not os.path.isdir(path):
            raise NotADirectoryError(f"'{path}' is a file, not a directory.")

        print(f"\n  Scanning directory: {path}\n")

        found_any = False

        for root, dirs, files in os.walk(path):
            level      = root.replace(path, "").count(os.sep)
            indent     = "    " * level
            sub_indent = "    " * (level + 1)

            print(f"  {indent}{os.path.basename(root)}/")

            for f in files:
                print(f"  {sub_indent}{f}")
                found_any = True

            if not files and not dirs:
                raise MissingFileOrFolderError(
                    f"Empty folder detected: {root}"
                )

        if not found_any:
            print("  [!] No files found in the directory.")

    except FileNotFoundError as e:
        print(f"  [!] Error : {e}")
    except NotADirectoryError as e:
        print(f"  [!] Error : {e}")
    except MissingFileOrFolderError as e:
        print(f"  [!] Custom Error : {e}")
    except PermissionError:
        print(f"  [!] Permission denied to access '{path}'.")
    except Exception as e:
        print(f"  [!] Unexpected Error : {e}")


def directory_scanner():
    print("\n" + "=" * 45)
    print("   MODULE 7 : Directory Scanner")
    print("=" * 45)

    sub_menu = """
  1. Scan a directory
  2. List only files in a directory
  3. Check if a file exists
  0. Back to main menu
  Choice : """

    while True:
        choice = input(sub_menu).strip()

        if choice == "1":
            path = input("  Enter directory path to scan : ").strip()
            scan_directory(path)

        elif choice == "2":
            path = input("  Enter directory path : ").strip()
            try:
                if not os.path.exists(path):
                    raise FileNotFoundError(f"Path not found: '{path}'")
                if not os.path.isdir(path):
                    raise NotADirectoryError(f"'{path}' is not a directory.")

                all_files = []
                for root, dirs, files in os.walk(path):
                    for f in files:
                        all_files.append(os.path.join(root, f))

                if not all_files:
                    print("  [!] No files found.")
                else:
                    print(f"\n  Files in '{path}' :")
                    for f in all_files:
                        print(f"    {f}")
                    print(f"\n  Total files found : {len(all_files)}")

            except FileNotFoundError as e:
                print(f"  [!] Error : {e}")
            except NotADirectoryError as e:
                print(f"  [!] Error : {e}")
            except Exception as e:
                print(f"  [!] Unexpected Error : {e}")

        elif choice == "3":
            file_path = input("  Enter full file path to check : ").strip()
            try:
                if not file_path:
                    raise ValueError("File path cannot be empty.")
                if os.path.exists(file_path):
                    if os.path.isfile(file_path):
                        size = os.path.getsize(file_path)
                        print(f"  [[OK]] File exists. Size : {size} bytes.")
                    else:
                        print(f"  [[OK]] Path exists but it is a directory, not a file.")
                else:
                    raise FileNotFoundError(f"'{file_path}' does not exist.")
            except FileNotFoundError as e:
                print(f"  [!] Error : {e}")
            except ValueError as e:
                print(f"  [!] Error : {e}")
            except Exception as e:
                print(f"  [!] Unexpected Error : {e}")

        elif choice == "0":
            break
        else:
            print("  [!] Invalid choice.")


# ============================================================
#  MAIN MENU - Dashboard
# ============================================================

MAIN_MENU = """
+-----------------------------------------------+
|     SMART CAMPUS INFORMATION SYSTEM           |
|     Main Application Dashboard                |
+-----------------------------------------------+
|  1. Student Registration & Grade Evaluation   |
|  2. Course Enrollment Management              |
|  3. Student Record Data Management            |
|  4. Sort & Search Student IDs                 |
|  5. Student Fee Calculation                   |
|  6. File Handling - Academic Records          |
|  7. Directory Scanner                         |
|  0. Exit                                      |
+-----------------------------------------------+
  Enter your choice : """


def main():
    print("\n  Welcome to the Smart Campus Information System")

    while True:
        choice = input(MAIN_MENU).strip()

        if   choice == "1": student_registration()
        elif choice == "2": course_enrollment()
        elif choice == "3": student_records()
        elif choice == "4": sort_search()
        elif choice == "5": fee_calculation()
        elif choice == "6": file_management()
        elif choice == "7": directory_scanner()
        elif choice == "0":
            print("\n  Thank you for using Smart Campus Information System. Goodbye!\n")
            break
        else:
            print("  [!] Invalid choice. Please select 0-7.")


if __name__ == "__main__":
    main()
