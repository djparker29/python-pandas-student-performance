import json
import os

import pandas as pd


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card


def main():
    data = []
    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card("students", student_number)
        
        total_grade = 0
        for subject in SUBJECTS:
            total_grade += report_card[subject]

        report_card["average_grade"] = total_grade / len(SUBJECTS)
        data.append(report_card)

    # Load report card data into a pandas dataframe
    df = pd.DataFrame(data)

    subject_grades = {}
    for subject in SUBJECTS:
        subject_grades[subject] = df[subject].mean()

    average_grade_scores = df.groupby("grade").mean()["average_grade"]

    print(f"Average Student Grade: {round(df['average_grade'].mean(), 2)}")
    print(f"Hardest Subject: {min(subject_grades, key=subject_grades.get)}")
    print(f"Easiest Subject: {max(subject_grades, key=subject_grades.get)}")
    print(f"Best Performing Grade: {average_grade_scores.idxmax()}")
    print(f"Worst Performing Grade: {average_grade_scores.idxmin()}")
    print(f"Best Student ID: {df['average_grade'].idxmax()}")
    print(f"Worst Student ID: {df['average_grade'].idxmin()}")


if __name__ == "__main__":
    main()
