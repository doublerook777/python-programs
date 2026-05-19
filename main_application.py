students        = []   # list of dicts  {name, age, grades}
enrolled_courses = []  # list of tuples (course_name, credits)
student_ids     = []   # list of ints

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

# LAB-1
def student_registration():
    print("\n" + "=" * 45)
    print("   MODULE 1 : Student Registration & Grade")
    print("=" * 45)

    name = input("Enter student name : ").strip()
    if not name:
        print("  [!] Name cannot be empty.")
        return

    try:
        score = float(input("Enter exam score (0–100) : "))
    except ValueError:
        print("  [!] Invalid score. Please enter a number.")
        return

    if not (0 <= score <= 100):
        print("  [!] Score must be between 0 and 100.")
        return

    grade, remark = get_grade(score)

    students.append({"name": name, "age": None, "grades": [score]})

    print("\n--- Student Report ---")
    print(f"  Name             : {name}")
    print(f"  Score            : {score}")
    print(f"  Grade            : {grade}")
    print(f"  Performance      : {remark}")

# LAB-2
def course_enrollment():
    print("\n" + "=" * 45)
    print("   MODULE 2 : Course Enrollment Management")
    print("=" * 45)

    MAX_COURSES = 5

    while True:
        if len(enrolled_courses) >= MAX_COURSES:
            print(f"  [!] Maximum course limit ({MAX_COURSES}) reached!")
            break

        course_name = input("\nEnter course name (or 'done' to finish) : ").strip()
        if course_name.lower() == "done":
            break
        if not course_name:
            print("  [!] Course name cannot be empty. Skipping...")
            continue

        credits_input = input("Enter credit value : ").strip()
        if not credits_input.isdigit():
            print("  [!] Invalid credit value! Skipping entry...")
            continue

        credits = int(credits_input)
        if credits <= 0:
            print("  [!] Credit must be positive! Skipping entry...")
            continue

        enrolled_courses.append((course_name, credits))
        print(f"  [✓] Course '{course_name}' with {credits} credit(s) added.")

    print("\n--- Enrollment Report ---")
    if not enrolled_courses:
        print("  No courses enrolled yet.")
    else:
        for course, credit in enrolled_courses:
            print(f"  Course : {course:<25}  Credits : {credit}")
        print(f"  Total courses enrolled : {len(enrolled_courses)}")

# LAB-3
def student_records():
    print("\n" + "=" * 45)
    print("   MODULE 3 : Student Record Management")
    print("=" * 45)

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

            students.append({"name": name, "age": age, "grades": grades})
            print(f"  [✓] Record for '{name}' added.")

        elif choice == "2":
            if not students:
                print("  No student records found.")
            else:
                print("\n=== Student Records ===")
                for s in students:
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

            print(f"\n  Common Participants       : {event_A & event_B}")
            print(f"  All Participants          : {event_A | event_B}")
            print(f"  Only in Event A           : {event_A - event_B}")
            print(f"  Only in Event B           : {event_B - event_A}")

        elif choice == "0":
            break
        else:
            print("  [!] Invalid choice.")

# LAB-4
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
                student_ids.extend(new_ids)
                print(f"  [✓] Added IDs : {new_ids}")
            except ValueError:
                print("  [!] Invalid input. Enter integers only.")

        elif choice == "2":
            print(f"  Current IDs : {student_ids}")

        elif choice == "3":
            if not student_ids:
                print("  [!] No IDs available. Add IDs first.")
            else:
                sorted_ids = bubble_sort(student_ids)
                print(f"  Sorted (Bubble Sort) : {sorted_ids}")

        elif choice == "4":
            if not student_ids:
                print("  [!] No IDs available. Add IDs first.")
            else:
                sorted_ids = selection_sort(student_ids)
                print(f"  Sorted (Selection Sort) : {sorted_ids}")

        elif choice == "5":
            if not student_ids:
                print("  [!] No IDs available.")
            else:
                try:
                    target = int(input("  Enter ID to search : "))
                    idx = linear_search(student_ids, target)
                    if idx != -1:
                        print(f"  [✓] Linear Search: ID {target} found at index {idx}.")
                    else:
                        print(f"  [✗] Linear Search: ID {target} not found.")
                except ValueError:
                    print("  [!] Invalid ID.")

        elif choice == "6":
            if not student_ids:
                print("  [!] No IDs available.")
            else:
                try:
                    target = int(input("  Enter ID to search : "))
                    sorted_ids = bubble_sort(student_ids)
                    idx = binary_search(sorted_ids, target)
                    if idx != -1:
                        print(f"  [✓] Binary Search: ID {target} found at index {idx} (in sorted list).")
                    else:
                        print(f"  [✗] Binary Search: ID {target} not found.")
                except ValueError:
                    print("  [!] Invalid ID.")

        elif choice == "0":
            break
        else:
            print("  [!] Invalid choice.")

# LAB-5
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    return tuition_fee + hostel_fee + transportation_fee


def fee_calculation():
    print("\n" + "=" * 45)
    print("   MODULE 5 : Student Fee Calculation")
    print("=" * 45)

    try:
        tuition = float(input("  Enter tuition fee (₹) : "))

        hostel_input = input("  Enter hostel fee (₹) [press Enter to skip] : ").strip()
        hostel = float(hostel_input) if hostel_input else 0

        transport_input = input("  Enter transportation fee (₹) [press Enter to skip] : ").strip()
        transport = float(transport_input) if transport_input else 0

    except ValueError:
        print("  [!] Invalid amount entered.")
        return

    total = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)

    print("\n--- Fee Breakdown ---")
    print(f"  Tuition Fee        : ₹ {tuition:,.2f}")
    print(f"  Hostel Fee         : ₹ {hostel:,.2f}")
    print(f"  Transportation Fee : ₹ {transport:,.2f}")
    print(f"  {'─'*30}")
    print(f"  Total Fee          : ₹ {total:,.2f}")

# LAB-6
FILE_NAME = "student_records.txt"


def write_records_to_file():
    try:
        with open(FILE_NAME, "w") as f:
            f.write("ID,Name,Marks\n")
            for i, s in enumerate(students, start=101):
                avg = sum(s["grades"]) / len(s["grades"]) if s["grades"] else 0
                f.write(f"{i},{s['name']},{avg:.1f}\n")
        print(f"  [✓] Records written to '{FILE_NAME}' successfully.")
    except Exception as e:
        print(f"  [!] Error writing file : {e}")


def read_records_from_file():
    try:
        with open(FILE_NAME, "r") as f:
            records = f.readlines()
        print("\n--- File Contents ---")
        for line in records:
            print(" ", line.strip())
        return records
    except FileNotFoundError:
        print(f"  [!] File '{FILE_NAME}' not found. Write records first.")
        return []
    except Exception as e:
        print(f"  [!] Error reading file : {e}")
        return []


def generate_report(records):
    if len(records) <= 1:
        print("  [!] No student data found in file.")
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
        print("  [!] No valid records to report.")
        return

    average = total_marks / total_students
    print("\n--- Performance Report ---")
    print(f"  Total Students  : {total_students}")
    print(f"  Average Marks   : {average:.2f}")
    print(f"  Top Student     : {top_student}  ({highest_marks} marks)")


def file_management():
    print("\n" + "=" * 45)
    print("   MODULE 6 : File Handling – Academic Records")
    print("=" * 45)

    sub_menu = """
  1. Write current student records to file
  2. Read records from file
  3. Generate performance report from file
  0. Back to main menu
  Choice : """

    while True:
        choice = input(sub_menu).strip()

        if choice == "1":
            if not students:
                print("  [!] No student records in memory. Register students first (Module 1 or 3).")
            else:
                write_records_to_file()

        elif choice == "2":
            read_records_from_file()

        elif choice == "3":
            records = read_records_from_file()
            if records:
                generate_report(records)

        elif choice == "0":
            break
        else:
            print("  [!] Invalid choice.")


MAIN_MENU = """
╔══════════════════════════════════════════════╗
║    SMART CAMPUS INFORMATION SYSTEM           ║
║    Main Application Dashboard                ║
╠══════════════════════════════════════════════╣
║  1. Student Registration & Grade Evaluation  ║
║  2. Course Enrollment Management             ║
║  3. Student Record Data Management           ║
║  4. Sort & Search Student IDs                ║
║  5. Student Fee Calculation                  ║
║  6. File Handling – Academic Records         ║
║  0. Exit                                     ║
╚══════════════════════════════════════════════╝
  Enter your choice : """


def main():
    print("\nWelcome to the Smart Campus Information System")

    while True:
        choice = input(MAIN_MENU).strip()

        if   choice == "1": student_registration()
        elif choice == "2": course_enrollment()
        elif choice == "3": student_records()
        elif choice == "4": sort_search()
        elif choice == "5": fee_calculation()
        elif choice == "6": file_management()
        elif choice == "0":
            print("\n  Thank you for using Smart Campus Information System. Goodbye!\n")
            break
        else:
            print("  [!] Invalid choice. Please select from the menu.")


if __name__ == "__main__":
    main()
