from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Mary Rose Godoyo's Flask API!"

# Student route
@app.route('/student')
def student():
    student_info = {
        "name": "Mary Rose Godoyo",
        "course": "BS Information Technology",
        "year": "4th Year"
    }
    return jsonify(student_info)

# Grade route
@app.route('/grade')
def grade():
    grades = {
        "Web Development": 95,
        "Database Systems": 92,
        "Artificial Intelligence": 90
    }
    return jsonify(grades)

# Course route
@app.route('/course')
def course():
    courses = [
        "Web Development",
        "Database Systems",
        "Artificial Intelligence",
        "System Integration"
    ]
    return jsonify(courses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
