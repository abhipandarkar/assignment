import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a route to handle the root URL ('/') and render the HTML page.
@app.route('/')
def home():
    # Generate the current date and time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Pass the dynamic content to the HTML template
    return render_template('ass.html', current_time=current_time)

# Define a route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
    # Get user data from the form
    name = request.form.get('name')
    email = request.form.get('email')

    # Store the submitted data in a text file
    with open('submissions.txt', 'a') as file:
        file.write(f"Name: {name}, Email: {email}\n")

    return redirect(url_for('submitted'))

# Define a route to display the submitted data
@app.route('/submitted')
def submitted():
    # Read and display the stored data from the text file
    submissions = []
    try:
        with open('submissions.txt', 'r') as file:
            submissions = file.readlines()
    except FileNotFoundError:
        pass

    return render_template('submit.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
