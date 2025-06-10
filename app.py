from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/book_appointment')
def book_appointment():
    return render_template('book_appointment.html')

@app.route('/video_call')
def video_call():
    return render_template('video_call.html')

if __name__ == '__main__':
    app.run(debug=True)