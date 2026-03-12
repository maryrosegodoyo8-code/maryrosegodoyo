from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API!"

@app.route('/student')
def student():
    return "Student API is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
