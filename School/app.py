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
            return render_template('dashboards/dashboard.html', username=username)
        
        elif role == 'staff' and username == 'staff' and password == 'password123':
            return render_template('dashboards/staff_dashboard.html', username=username, role=role)
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
        
    return render_template('dashboards/dashboard.html', username=session['username'])

# -- PROTECTED ROUTE: STUDENT DASH ---
ROOMS = [
    {"id": 1, "name": "Lecture Theatre 1", "type": "lecture", "desc": "Large capacity theatre for presentations."},
    {"id": 2, "name": "Computer Lab A", "type": "lab", "desc": "Equipped with high-end workstations."},
    {"id": 3, "name": "Main Hall", "type": "multipurpose", "desc": "Open space for events and gatherings."},
    {"id": 4, "name": "Quiet Zone 4", "type": "study", "desc": "Individual study pods with power outlets."},
    {"id": 5, "name": "Science Lab B", "type": "lab", "desc": "Chemistry equipment and safety stations."},
    {"id": 6, "name": "Study Room 2", "type": "study", "desc": "Group discussion table and whiteboard."}
]

@app.route('/')
def dashboard():
    room_type = request.args.get('type', 'all')
    
    # Filtering logic
    if room_type == 'all' or not room_type:
        filtered_rooms = ROOMS
    else:
        filtered_rooms = [r for r in ROOMS if r['type'] == room_type]
        
    return render_template('dashboard.html', 
                           rooms=filtered_rooms, 
                           current_filter=room_type,
                           username="Student John Doe", 
                           student_id="7654321")

@app.route('/book/<int:room_id>')
def book_room(room_id):
    # Success message for booking
    flash(f"Room {room_id} has been successfully booked!")
    return redirect(url_for('dashboard'))

# --- PROTECTED ROUTE: STAFF AREA ---
@app.route('/staff')
def staff_dashboard():
    # 1. Check if they are logged in. 2. Check if their role is exactly 'staff'.
    if 'role' not in session or session['role'] != 'staff':
        # If they fail the check, boot them out!
        flash("Access Denied: You must be logged in as Staff to view this page.")
        return redirect(url_for('login'))
        
    return render_template('dashboards/staff_dashboard.html', username=session['username'])


# --- PROTECTED ROUTE: STAFF DASH ---
app.secret_key = "uow_staff_secret_key"

# Sample Data simulating existing rooms
EXISTING_ROOMS = [
    {"id": 1, "name": "Lecture Theatre 1", "type": "lecture", "desc": "Large capacity theatre.", "capacity": 200},
    {"id": 2, "name": "Computer Lab A", "type": "lab", "desc": "High-end workstations.", "capacity": 30},
    {"id": 3, "name": "Quiet Zone 4", "type": "study", "desc": "Individual study pods.", "capacity": 1}
]

# Common user data for the sidebar
USER_INFO = {
    "username": "Staff Member",
    "id": "STAFF001",
    "role": "staff" # Crucial for future access control
}

@app.route('/')
def index():
    # Redirect to the main staff dashboard grid by default
    return redirect(url_for('staff_dashboard'))

@app.route('/staff/dashboard')
def staff_dashboard():
    """
    Shows the grid of existing rooms.
    """
    return render_template('staff_grid.html', 
                           rooms=EXISTING_ROOMS, 
                           user=USER_INFO,
                           title="Staff Room Creation")

@app.route('/staff/create-room', methods=['GET', 'POST'])
def create_room():
    """
    GET: Shows the blank form.
    POST: Simulates saving the data and redirects back to the grid.
    """
    if request.method == 'POST':
        # Simulate saving the data from the form
        room_name = request.form.get('room_name')
        flash(f"Room '{room_name}' has been simulated as created!", "success")
        return redirect(url_for('staff_dashboard'))
        
    return render_template('staff_form.html', 
                           user=USER_INFO,
                           title="Room Creation Form")
    
# --- LOGOUT ROUTE ---
@app.route('/logout')
def logout():
    session.clear() # This deletes everything in the session vault
    flash("You have been safely logged out.")
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Start the web server in debug mode so it updates when you change code
    app.run(debug=True)
    