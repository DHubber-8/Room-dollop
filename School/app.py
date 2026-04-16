# app.py
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# A secret key is required by Flask to display flash messages safely
app.secret_key = "super_secret_school_key" 

@app.route('/', methods=['GET', 'POST'])
def login():
    # If the user clicks the "Login" button, it sends a POST request
    if request.method == 'POST':
        # Grab the data the user typed into the form
        username = request.form['username']
        password = request.form['password']
        role = request.form.get('role', 'student') # Defaults to student if empty
        
        # Check if the credentials match our dummy data
        if username == 'student' and password == 'password123':
            return render_template('dashboard.html', username=username)
        
        elif role == 'staff' and username == 'staff' and password == 'password123':
            return render_template('dashboard.html', username=username, role=role)
        else:
            # If wrong, send an error message back to the page
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('login'))
            
    # If they are just visiting the page (GET request), show the login form
    return render_template('login.html')

# --- PROTECTED ROUTE: STUDENT AREA ---
@app.route('/student')
def student_dashboard():
    # 1. Check if they are logged in. 2. Check if their role is exactly 'student'.
    if 'role' not in session or session['role'] != 'student':
        # If they fail the check, boot them out!
        flash("Access Denied: You must be logged in as a Student to view this page.")
        return redirect(url_for('login'))
        
    return render_template('student_dashboard.html', username=session['username'])

# --- PROTECTED ROUTE: STAFF AREA ---
@app.route('/staff')
def staff_dashboard():
    # 1. Check if they are logged in. 2. Check if their role is exactly 'staff'.
    if 'role' not in session or session['role'] != 'staff':
        # If they fail the check, boot them out!
        flash("Access Denied: You must be logged in as Staff to view this page.")
        return redirect(url_for('login'))
        
    return render_template('staff_dashboard.html', username=session['username'])

# --- LOGOUT ROUTE ---
@app.route('/logout')
def logout():
    session.clear() # This deletes everything in the session vault
    flash("You have been safely logged out.")
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Start the web server in debug mode so it updates when you change code
    app.run(debug=True)