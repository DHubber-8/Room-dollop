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
        
        # Check if the credentials match our dummy data
        if username == 'student' and password == 'password123':
            return render_template('dashboard.html', username=username)
        else:
            # If wrong, send an error message back to the page
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('login'))
            
    # If they are just visiting the page (GET request), show the login form
    return render_template('login.html')

if __name__ == '__main__':
    # Start the web server in debug mode so it updates when you change code
    app.run(debug=True)