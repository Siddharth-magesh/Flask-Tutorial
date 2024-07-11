from flask import Flask, request, render_template
import mysql.connector

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page, which displays the form
@app.route('/')
def form():
    return render_template('index.html')

# Define the route for form submission, which inserts data into the database
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data from the request
    name = request.form['name']
    age = request.form['age']
    salary = request.form['salary']
    
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root', 
            password='',  # Add your MySQL password here
            database='mydatabase'
        )
        
        # Create a new database cursor
        cursor = conn.cursor()
        
        # Define the SQL query for inserting data
        query = "INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)"
        
        # Execute the SQL query with the form data
        cursor.execute(query, (name, age, salary))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Return a success message
        return "Data inserted successfully"
    except mysql.connector.Error as err:
        # Handle any errors that occur during the database interaction
        return f"Error: {err}"

# Define the route for another page, which displays a different template
@app.route('/another_page')
def another_page():
    return render_template('display.html')

# Define the route for fetching data from the database
@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    # Get the name from the form data
    name = request.form['name']

    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root', 
            password='',  # Add your MySQL password here
            database='mydatabase'
        )
        
        # Create a new database cursor
        cursor = conn.cursor()
        
        # Define the SQL query for fetching data
        query = "SELECT name, age, salary FROM employees WHERE name = %s"
        
        # Execute the SQL query with the form data
        cursor.execute(query, (name,))
        
        # Fetch the result of the query
        result = cursor.fetchone()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()

        if result:
            # If data is found, create a dictionary to hold the data
            data = {
                'name': result[0],
                'age': result[1],
                'salary': result[2]
            }
            # Render the template with the fetched data
            return render_template('display.html', data=data)
        else:
            # If no data is found, render the template with a message
            return render_template('display.html', data=None, message="No data found for the given name.")
    
    except mysql.connector.Error as err:
        # Handle any errors that occur during the database interaction
        return f"Error: {err}"

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
