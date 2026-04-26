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

@app.route('/student_dashboard')
def student_dashboard():
    # Security check: Ensure the user is actually logged in as a student
    if 'role' not in session or session['role'] != 'student':
        flash("Access Denied: You must be logged in as a Student to view this page.")
        return redirect(url_for('home'))
    
    rooms_database = student_system.get_available_rooms()

    return render_template('StudentDashboard.html', username=session['username'], rooms=rooms_database)


@app.route('/staff_dashboard')
def staff_dashboard():
    # Security check: Ensure the user is actually logged in as a staff
    if 'role' not in session or session['role'] != 'staff':
        flash("Access Denied: You must be logged in as a Staff to view this page.")
        return redirect(url_for('home'))
    
    rooms_database = staff_system.get_all_rooms()
    
    return render_template('StaffDashboard.html', username=session['username'], rooms=rooms_database)

# --- LOGOUT ROUTE ---
@app.route('/logout')
def logout():
    # 1. Remove the user's data from the session dictionary
    # The 'None' part just prevents an error if the data is already gone
    session.pop('username', None)
    session.pop('role', None)
    
    # Note: If you want to completely wipe the entire cookie at once, 
    # you can just use `session.clear()` instead of the pop lines above!

    # 2. Add a friendly message
    flash("You have been successfully logged out.")

    # 3. "Loopback" to the login page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)