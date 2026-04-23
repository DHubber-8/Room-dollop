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
            return redirect(url_for('student_dashboard')) # We can link a real page later
            
        elif role == 'staff' and check_staff_login(username, password):
            session['username'] = username
            session['role'] = 'staff'
            return redirect(url_for('staff_dashboard')) # We can link a real page later
            
        else:
            flash(f'Invalid {role} username or password. Please try again.')
            return redirect(url_for('home'))
            
    # Pointing to Home.html inside your Web UI folder
    return render_template('Home.html') 


@app.route('/student_dashboard')
def student_dashboard():
    # Security check: Ensure the user is actually logged in as a student
    if 'role' not in session or session['role'] != 'student':
        flash("Access Denied: You must be logged in as a Student to view this page.")
        return redirect(url_for('home'))
    
    rooms_database = [
        {"id": 1, "name": "Lecture Hall B.1.1", "category": "Lecture Hall", "time": "09:00AM - 10:00AM", "desc": "Large seating, capacity 200"},
        {"id": 2, "name": "Computer Lab A.2.3", "category": "Computer Lab", "time": "10:00AM - 11:00AM", "desc": "Equipped with 30 PCs"},
        {"id": 3, "name": "Study Room A.3.5", "category": "Study Room", "time": "11:00AM - 12:00PM", "desc": "Small room, capacity 5"},
        {"id": 4, "name": "Lecture Hall B.1.2", "category": "Lecture Hall", "time": "01:00PM - 02:00PM", "desc": "Medium seating, capacity 100"},
        {"id": 5, "name": "Computer Lab A.2.4", "category": "Computer Lab", "time": "02:00PM - 03:00PM", "desc": "Equipped with 20 PCs"},
        {"id": 6, "name": "Meeting Room A.3.6", "category": "Meeting Room", "time": "03:00PM - 04:00PM", "desc": "Medium room, capacity 10"}
        ]

    return render_template('StudentDashboard.html', username=session['username'], rooms=rooms_database)


if __name__ == '__main__':
    app.run(debug=True)