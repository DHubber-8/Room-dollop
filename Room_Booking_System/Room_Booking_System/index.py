# Logic/index.py
from flask import Flask, render_template, request, redirect, url_for, flash, session

from Logic.Student.Student import Student
from Logic.Staff.Staff import Staff

app = Flask(__name__, template_folder='Web UI', static_folder='Web UI')
app.secret_key = "super_secret_school_key"

student_system = Student()
staff_system = Staff()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form.get('role', 'student') 
        
        if role == 'student' and student_system.check_student_login(username, password):
            session['username'] = username
            session['role'] = 'student'
            return redirect(url_for('student_dashboard')) # can link a real page later
            
        elif role == 'staff' and staff_system.check_staff_login(username, password):
            session['username'] = username
            session['role'] = 'staff'
            return redirect(url_for('staff_dashboard')) # can link a real page later
            
    return render_template('Home.html')

# --- RESET PASSWORD ROUTE ---
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        username = request.form.get('username')
        
        flash(f"If the username '{username}' exists, a password reset link has been sent to the registered email.")
        return redirect(url_for('home'))
        
    # If the user just clicked the "Forget Password" link, show them the page
    return render_template('ResetPassword.html')

@app.route('/student_dashboard')
def student_dashboard():
    if 'role' not in session or session['role'] != 'student':
        flash("Access Denied: You must be logged in as a Student to view this page.")
        return redirect(url_for('home'))
    
    rooms_database = student_system.get_available_rooms()
    bookings_database = student_system.get_current_bookings(session['username'])
    return render_template('StudentDashboard.html', username=session['username'], rooms=rooms_database, bookings=bookings_database)

@app.route('/staff_dashboard')
def staff_dashboard():
    if 'role' not in session or session['role'] != 'staff':
        flash("Access Denied: You must be logged in as a Staff to view this page.")
        return redirect(url_for('home'))
    
    rooms_database = staff_system.get_all_rooms()
    return render_template('StaffDashboard.html', username=session['username'], rooms=rooms_database)

# --- LOGOUT ROUTE ---
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    flash("You have been successfully logged out.")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)