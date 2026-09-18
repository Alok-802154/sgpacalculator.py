from flask import Flask, render_template, request

app = Flask(__name__)

subjects = [
    ("Open Elective", 3),
    ("Electronic Devices", 3),
    ("Digital Logic Design", 3),
    ("Electronics Devices Lab", 1),
    ("Digital Logic Design Lab", 1),
    ("Industrial Engineering", 3),
    ("Transmission Lines & Electromagnetic Waves", 3),
    ("Networks, Signals and Systems", 3)
]

def get_grade_point(marks):
    if marks >= 91:
        return 10
    elif marks >= 81:
        return 9
    elif marks >= 71:
        return 8
    elif marks >= 61:
        return 7
    elif marks >= 51:
        return 6
    elif marks >= 45:
        return 5
    elif marks >= 40:
        return 4
    else:
        return 0


@app.route("/", methods=["GET", "POST"])
def index():
    sgpa = None
    total_points = None
    error = None

    if request.method == "POST":
        total_points = 0
        total_credits = 0

        try:
            for i, (subject, credit) in enumerate(subjects):
                marks = float(request.form[f"marks_{i}"])

                if marks < 0 or marks > 100:
                    raise ValueError("Marks must be between 0 and 100.")

                grade_point = get_grade_point(marks)
                total_points += credit * grade_point
                total_credits += credit

            sgpa = total_points / total_credits

        except ValueError as e:
            error = str(e)
            total_points = None

    return render_template(
        "index.html",
        subjects=subjects,
        sgpa=sgpa,
        total_points=total_points,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)