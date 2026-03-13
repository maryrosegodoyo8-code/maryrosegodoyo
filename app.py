from flask import Flask, jsonify, request, render_template_string, redirect, url_for

app = Flask(__name__)

students = [
    {"id": 1, "name": "Juan", "grade": 85, "section": "Stallman"},
    {"id": 2, "name": "Maria", "grade": 90, "section": "Stallman"}
]

# HOME PAGE
@app.route('/')
def home():
    html = """
    <html>
    <head>
    <title>Student Dashboard</title>
    <style>

    body{
        font-family: Arial;
        background: linear-gradient(135deg,#1d2671,#c33764);
        color:white;
        text-align:center;
        margin:0;
    }

    header{
        padding:20px;
        font-size:30px;
        font-weight:bold;
        background:rgba(0,0,0,0.2);
    }

    .container{
        margin:40px auto;
        width:80%;
        background:white;
        color:black;
        padding:30px;
        border-radius:10px;
        box-shadow:0 10px 20px rgba(0,0,0,0.2);
    }

    a{
        text-decoration:none;
        padding:10px 20px;
        background:#3498db;
        color:white;
        border-radius:5px;
        margin:10px;
        display:inline-block;
    }

    a:hover{
        background:#2980b9;
    }

    </style>
    </head>

    <body>

    <header>Student Management API</header>

    <div class="container">
    <h2>Welcome to the Student Dashboard</h2>

    <a href="/students_page">View Students</a>
    <a href="/add_student_form">Add Student</a>

    </div>

    </body>
    </html>
    """
    return render_template_string(html)


# STUDENTS TABLE PAGE
@app.route('/students_page')
def students_page():

    rows = ""
    for s in students:
        rows += f"""
        <tr>
            <td>{s['id']}</td>
            <td>{s['name']}</td>
            <td>{s['grade']}</td>
            <td>{s['section']}</td>
        </tr>
        """

    html = f"""
    <html>
    <head>
    <title>Students List</title>

    <style>

    body {{
        font-family:Arial;
        background:#f4f6f9;
        text-align:center;
    }}

    h1 {{
        background:#2c3e50;
        color:white;
        padding:20px;
        margin:0;
    }}

    table {{
        margin:40px auto;
        border-collapse:collapse;
        width:70%;
        background:white;
        box-shadow:0 5px 10px rgba(0,0,0,0.2);
    }}

    th,td {{
        padding:12px;
        border-bottom:1px solid #ddd;
    }}

    th {{
        background:#3498db;
        color:white;
    }}

    tr:hover {{
        background:#f1f1f1;
    }}

    a {{
        text-decoration:none;
        padding:10px 15px;
        background:#27ae60;
        color:white;
        border-radius:5px;
    }}

    </style>

    </head>

    <body>

    <h1>Students List</h1>

    <table>

    <tr>
    <th>ID</th>
    <th>Name</th>
    <th>Grade</th>
    <th>Section</th>
    </tr>

    {rows}

    </table>

    <a href="/">Back to Dashboard</a>

    </body>
    </html>
    """

    return render_template_string(html)


# ADD STUDENT FORM
@app.route('/add_student_form')
def form():

    html = """
    <html>
    <head>
    <title>Add Student</title>

    <style>

    body{
        font-family:Arial;
        background:linear-gradient(135deg,#2c3e50,#4ca1af);
        text-align:center;
        color:white;
    }

    .form-box{
        background:white;
        color:black;
        width:400px;
        margin:80px auto;
        padding:30px;
        border-radius:10px;
        box-shadow:0 10px 20px rgba(0,0,0,0.3);
    }

    input{
        width:90%;
        padding:10px;
        margin:10px;
        border:1px solid #ccc;
        border-radius:5px;
    }

    button{
        padding:10px 20px;
        background:#3498db;
        border:none;
        color:white;
        border-radius:5px;
        cursor:pointer;
    }

    button:hover{
        background:#2980b9;
    }

    </style>

    </head>

    <body>

    <div class="form-box">

    <h2>Add Student</h2>

    <form action="/add_student" method="POST">

    <input type="text" name="name" placeholder="Student Name" required>

    <input type="number" name="grade" placeholder="Grade" required>

    <input type="text" name="section" placeholder="Section" required>

    <br><br>

    <button type="submit">Add Student</button>

    </form>

    <br>
    <a href="/">Back</a>

    </div>

    </body>
    </html>
    """

    return render_template_string(html)


# ADD STUDENT FUNCTION
@app.route('/add_student', methods=['POST'])
def add_student():

    name = request.form.get("name")
    grade = int(request.form.get("grade"))
    section = request.form.get("section")

    new_student = {
        "id": len(students) + 1,
        "name": name,
        "grade": grade,
        "section": section
    }

    students.append(new_student)

    return redirect(url_for('students_page'))


# API JSON
@app.route('/students')
def students_list():
    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=True)
