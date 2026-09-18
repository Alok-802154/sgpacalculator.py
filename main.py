import tkinter as tk
from tkinter import messagebox


# =========================================================
# GRADE POINT SYSTEM
# =========================================================

def get_grade_point(marks):

    if 91 <= marks <= 100:
        return 10

    elif 81 <= marks <= 90:
        return 9

    elif 71 <= marks <= 80:
        return 8

    elif 61 <= marks <= 70:
        return 7

    elif 51 <= marks <= 60:
        return 6

    elif 45 <= marks <= 50:
        return 5

    elif 40 <= marks <= 44:
        return 4

    else:
        return 0


# =========================================================
# SUBJECTS
# =========================================================

subjects = [
    ("Open Elective", 3, "Theory"),
    ("Electronic Devices", 3, "Theory"),
    ("Digital Logic Design", 3, "Theory"),
    ("Electronics Devices Lab", 1, "Practical"),
    ("Digital Logic Design Lab", 1, "Practical"),
    ("Industrial Engineering", 3, "Theory"),
    ("Transmission Lines & Electromagnetic Waves", 3, "Theory"),
    ("Networks, Signals and Systems", 3, "Theory")
]

TOTAL_CREDITS = 20


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("B.Tech ECE - Semester 3 SGPA Calculator")

root.geometry("1050x720")

root.resizable(False, False)

root.configure(bg="#eef5ff")


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    root,
    bg="#1565c0",
    height=115
)

header.pack(fill="x")

header.pack_propagate(False)


tk.Label(
    header,
    text="B.Tech ECE",
    font=("Arial", 28, "bold"),
    bg="#1565c0",
    fg="white"
).pack(pady=(15, 2))


tk.Label(
    header,
    text="Semester 3 SGPA Calculator",
    font=("Arial", 19, "bold"),
    bg="#1565c0",
    fg="white"
).pack()


tk.Label(
    header,
    text="Enter obtained marks for each subject",
    font=("Arial", 11),
    bg="#1565c0",
    fg="white"
).pack(pady=3)


# =========================================================
# TABLE
# =========================================================

table = tk.Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)

table.pack(
    padx=20,
    pady=20
)


headers = [
    "Subject",
    "Type",
    "Credits",
    "Obtained Marks",
    "Grade Point"
]

widths = [38, 12, 10, 18, 15]


for column, heading in enumerate(headers):

    tk.Label(
        table,
        text=heading,
        font=("Arial", 10, "bold"),
        bg="#1565c0",
        fg="white",
        width=widths[column],
        pady=10
    ).grid(
        row=0,
        column=column,
        sticky="nsew"
    )


# =========================================================
# ENTRY AND GRADE POINT LIST
# =========================================================

mark_entries = []
grade_point_labels = []


# =========================================================
# SUBJECT ROWS
# =========================================================

for row, (subject, credit, course_type) in enumerate(
        subjects, start=1):

    # Subject name
    tk.Label(
        table,
        text=subject,
        font=("Arial", 10),
        bg="white",
        anchor="w",
        width=widths[0]
    ).grid(
        row=row,
        column=0,
        padx=5,
        pady=7,
        sticky="w"
    )


    # Type
    tk.Label(
        table,
        text=course_type,
        font=("Arial", 10),
        bg="white",
        fg="#64748b",
        width=widths[1]
    ).grid(
        row=row,
        column=1
    )


    # Credits
    tk.Label(
        table,
        text=str(credit),
        font=("Arial", 10, "bold"),
        bg="white",
        width=widths[2]
    ).grid(
        row=row,
        column=2
    )


    # Marks Entry
    entry = tk.Entry(
        table,
        font=("Arial", 11),
        width=12,
        justify="center",
        bd=1,
        relief="solid"
    )

    entry.grid(
        row=row,
        column=3,
        padx=5,
        pady=7
    )

    mark_entries.append(entry)


    # Grade Point
    grade_label = tk.Label(
        table,
        text="-",
        font=("Arial", 11, "bold"),
        bg="white",
        fg="#1565c0",
        width=widths[4]
    )

    grade_label.grid(
        row=row,
        column=4
    )

    grade_point_labels.append(grade_label)


# =========================================================
# AUTOMATIC GRADE POINT WHEN MARKS ARE ENTERED
# =========================================================

def update_grade_point(event=None):

    for i, entry in enumerate(mark_entries):

        value = entry.get().strip()

        if value == "":
            grade_point_labels[i].config(text="-")
            continue

        try:

            marks = float(value)

            if 0 <= marks <= 100:

                point = get_grade_point(marks)

                grade_point_labels[i].config(
                    text=str(point)
                )

            else:

                grade_point_labels[i].config(
                    text="Invalid"
                )

        except ValueError:

            grade_point_labels[i].config(
                text="Invalid"
            )


# Bind typing to all entries
for entry in mark_entries:

    entry.bind(
        "<KeyRelease>",
        update_grade_point
    )


# =========================================================
# RESULT FRAME
# =========================================================

result_frame = tk.Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)

result_frame.pack(
    padx=20,
    pady=5,
    fill="x"
)


# Total Credits
tk.Label(
    result_frame,
    text="Total Credits",
    font=("Arial", 11),
    bg="white",
    fg="#64748b"
).grid(
    row=0,
    column=0,
    pady=(12, 2)
)


tk.Label(
    result_frame,
    text="20",
    font=("Arial", 16, "bold"),
    bg="white"
).grid(
    row=1,
    column=0,
    pady=(0, 12)
)


# Total Grade Points
tk.Label(
    result_frame,
    text="Total Credit × Grade Point",
    font=("Arial", 11),
    bg="white",
    fg="#64748b"
).grid(
    row=0,
    column=1,
    pady=(12, 2)
)


total_points_label = tk.Label(
    result_frame,
    text="0.00",
    font=("Arial", 16, "bold"),
    bg="white"
)

total_points_label.grid(
    row=1,
    column=1,
    pady=(0, 12)
)


# SGPA
tk.Label(
    result_frame,
    text="SGPA",
    font=("Arial", 11),
    bg="white",
    fg="#64748b"
).grid(
    row=0,
    column=2,
    pady=(12, 2)
)


sgpa_label = tk.Label(
    result_frame,
    text="0.00",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="#1565c0"
)

sgpa_label.grid(
    row=1,
    column=2,
    pady=(0, 12)
)


# =========================================================
# CALCULATE SGPA
# =========================================================

def calculate_sgpa():

    total_points = 0

    # Check every subject
    for i, entry in enumerate(mark_entries):

        value = entry.get().strip()

        if value == "":

            messagebox.showwarning(
                "Marks Missing",
                f"Please enter marks for:\n{subjects[i][0]}"
            )

            entry.focus()

            return

        try:

            marks = float(value)

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                f"Please enter valid marks for:\n{subjects[i][0]}"
            )

            entry.focus()

            return


        if marks < 0 or marks > 100:

            messagebox.showerror(
                "Invalid Marks",
                f"Marks must be between 0 and 100.\n\n"
                f"Subject: {subjects[i][0]}"
            )

            entry.focus()

            return


        # Get grade point
        point = get_grade_point(marks)


        # Credit
        credit = subjects[i][1]


        # Credit × Grade Point
        total_points += credit * point


        # Update displayed grade point
        grade_point_labels[i].config(
            text=str(point)
        )


    # =====================================================
    # SGPA FORMULA
    # =====================================================

    sgpa = total_points / TOTAL_CREDITS


    # Display results

    total_points_label.config(
        text=f"{total_points:.2f}"
    )

    sgpa_label.config(
        text=f"{sgpa:.2f}"
    )


# =========================================================
# RESET
# =========================================================

def reset_calculator():

    for entry in mark_entries:

        entry.delete(
            0,
            tk.END
        )


    for label in grade_point_labels:

        label.config(
            text="-"
        )


    total_points_label.config(
        text="0.00"
    )


    sgpa_label.config(
        text="0.00"
    )


# =========================================================
# BUTTONS
# =========================================================

button_frame = tk.Frame(
    root,
    bg="#eef5ff"
)

button_frame.pack(
    pady=12
)


tk.Button(
    button_frame,
    text="Calculate SGPA",
    command=calculate_sgpa,
    font=("Arial", 12, "bold"),
    bg="#1565c0",
    fg="white",
    padx=25,
    pady=10,
    cursor="hand2"
).grid(
    row=0,
    column=0,
    padx=10
)


tk.Button(
    button_frame,
    text="Reset",
    command=reset_calculator,
    font=("Arial", 12, "bold"),
    bg="#64748b",
    fg="white",
    padx=35,
    pady=10,
    cursor="hand2"
).grid(
    row=0,
    column=1,
    padx=10
)


# =========================================================
# GRADING INFORMATION
# =========================================================

tk.Label(
    root,
    text=(
        "91-100 = 10   |   "
        "81-90 = 9   |   "
        "71-80 = 8   |   "
        "61-70 = 7   |   "
        "51-60 = 6   |   "
        "45-50 = 5   |   "
        "40-44 = 4   |   "
        "<40 = 0"
    ),
    font=("Arial", 10),
    bg="#eef5ff",
    fg="#475569"
).pack(
    pady=5
)


# Formula

tk.Label(
    root,
    text="SGPA = Σ (Credit × Grade Point) ÷ Total Credits",
    font=("Arial", 11, "bold"),
    bg="#eef5ff",
    fg="#1565c0"
).pack()


# =========================================================
# START
# =========================================================

root.mainloop()