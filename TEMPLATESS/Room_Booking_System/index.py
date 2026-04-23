# Logic/index.py
from flask import Flask, render_template, request, redirect, url_for, flash, session

from Logic.Student.Student import check_student_login
from Logic.Staff.Staff import check_staff_login

app = Flask(__name__, template_folder='Web UI', static_folder='Web UI')
app.secret_key = "super_secret_school_key" 

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form.get('role', 'student') 
        
        # 3. Use your imported functions to check the login
        if role == 'student' and check_student_login(username, password):
            session['username'] = username
            session['role'] = 'student'
            return "Welcome to the Student Booking Dashboard!" # We can link a real page later
            
        elif role == 'staff' and check_staff_login(username, password):
            session['username'] = username
            session['role'] = 'staff'
            return "Welcome to the Staff Dashboard!" # We can link a real page later
            
        else:
            flash(f'Invalid {role} username or password. Please try again.')
            return redirect(url_for('home'))
            
    # Pointing to Home.html inside your Web UI folder
    return render_template('Home.html') 

if __name__ == '__main__':
    app.run(debug=True)