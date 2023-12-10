# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class and assign it to the variable 'app'
app = Flask(__name__)

# Define a route for the root URL ("/") of the web application
@app.route('/') 
def Welcome():
    """
    A Flask route function for the root URL.

    When someone visits the root URL of the website, this function is called.
    It returns a simple welcome message.

    Returns:
        str: A welcome message.
    """
    return "Welcome to the Flask Tutorial"

# Define a route for the "/secondpage" URL of the web application
@app.route('/secondpage')
def secondpage():
    """
    A Flask route function for the "/secondpage" URL.

    When someone visits the "/secondpage" URL, this function is called.
    It returns a message indicating that this is the second page of the website.

    Returns:
        str: A message for the second page.
    """
    return "This is the second page of the website"

# Check if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
