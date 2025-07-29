# Anna University SGPA Calculator - Project Version
import datetime

grade_to_point = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "RA": 0
}

classification = {
    (9.0, 10): "Outstanding",
    (8.0, 8.99): "Excellent",
    (7.0, 7.99): "Very Good",
    (6.0, 6.99): "Good",
    (5.0, 5.99): "Average",
    (0, 4.99): "Fail"
}

def get_classification(sgpa):
    for (low, high), title in classification.items():
        if low <= sgpa <= high:
            return title
    return "Unknown"

def calculate_sgpa(subjects):
    total_score = 0
    total_credits = 0
    for sub in subjects:
        point = grade_to_point.get(sub["grade"], 0)
        total_score += point * sub["credit"]
        total_credits += sub["credit"]
    return total_score / total_credits if total_credits else 0

def display_report(subjects, sgpa):
    print("\n📘 Subject Details:")
    for i, sub in enumerate(subjects, start=1):
        print(f"{i}. {sub['name']} - Grade: {sub['grade']} | Credit: {sub['credit']}")

    print(f"\n🎯 SGPA: {sgpa:.2f}")
    print(f"📊 Performance: {get_classification(sgpa)}")

def save_to_file(name, roll, subjects, sgpa):
    filename = f"{name}_SGPA_Report.txt"
    with open(filename, "w") as f:
        f.write(f"SGPA Report for {name} ({roll})\n")
        f.write(f"Date: {datetime.date.today()}\n\n")
        f.write("Subject-wise Details:\n")
        for sub in subjects:
            f.write(f"{sub['name']} - Grade: {sub['grade']} | Credit: {sub['credit']}\n")
        f.write(f"\nFinal SGPA: {sgpa:.2f}\n")
        f.write(f"Performance: {get_classification(sgpa)}\n")
    print(f"\n📝 Report saved as {filename}")

def main():
    print("🔢 Anna University SGPA Calculator")
    name = input("Enter your name: ")
    roll = input("Enter your roll number: ")
    subjects = []

    num_subjects = int(input("\nEnter number of subjects: "))
    for _ in range(num_subjects):
        subject_name = input("Subject name: ")
        grade = input("Grade (O, A+, A, B+, B, RA): ").upper().strip()
        while grade not in grade_to_point:
            grade = input("❌ Invalid grade. Enter again (O, A+, A, B+, B, RA): ").upper().strip()
        credit = int(input("Credit: "))
        subjects.append({
            "name": subject_name,
            "grade": grade,
            "credit": credit
        })

    sgpa = calculate_sgpa(subjects)
    display_report(subjects, sgpa)
    save_to_file(name, roll, subjects, sgpa)

if __name__ == "__main__":
    main()
