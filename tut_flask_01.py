"""
@author = hari
@email  = harihararajanrm.cms@gmail.com 
-----------------------------------------
Topics covered in this tutorial
- Building URL Dynamically
- Variable Rules and URL building
"""
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the second tutorial on Flasks"

@app.route('/success/<int:score>') # dynamic URL RULES: '/success/<datatype:arg to function>'
# <int:score> signifies that there's a dynamic parameter named score, and it is expected to be an integer.
def success(score:int): # score is the dynamic parameter
    return f"The person has passed the flask test and the score is {score}"

@app.route('/fail/<int:score>') # dynamic URL RULES
def fail(score:int):
    return f"the person has failed the flask test and the score is {score}"

@app.route('/results/<int:Marks>') # dynamic URL RUL
def results(Marks):
    """
    A Flask route function for the "/results/<int:Marks>" URL.

    Parameters:
        Marks (int): The score obtained.

    When someone visits a URL like "/results/75", this function is called with the provided Marks.
    It determines the result (success or fail) based on the score and redirects to the corresponding page.

    Args:
        Marks (int): The score obtained by the person.

    Returns:
        Flask.redirect: Redirects to the 'success' or 'fail' page based on the determined result.
    """
    
    result =""
    if Marks >= 50:
        result ="success"
    else:
        result ="fail"
    
    return redirect(url_for(result, score=Marks)) # as success/fail page takes score as a parameter, we
#  need to pass the result generated within the results function

if __name__ == '__main__':
    app.run(debug=True)

"""
Documentation:
run the tut_flask_01.py using <python tut_flask_01.py>
click the URL in the terminal will take you to the home page
Root Page ("/"):

To visit the root page, open your web browser and navigate to http://localhost:5000/ (assuming default Flask settings).
You will see the welcome message for the second Flask tutorial.

Success Page ("/success/int:score") - Dynamic URL:

To visit the success page with a specific score, replace <score> with an integer of your choice.
For example, to visit the success page with a score of 85, navigate to http://localhost:5000/success/85.
Fail Page ("/fail/int:score") - Dynamic URL:

Fail Page ("/fail/int:score") - Dynamic URL:

To visit the fail page with a specific score, replace <score> with an integer of your choice.
For example, to visit the fail page with a score of 40, navigate to http://localhost:5000/fail/40.
Remember to adapt the URLs based on the port number and domain where your Flask app is running. 
This documentation should help users understand how to navigate to different pages on the web using the provided
Flask routes.

"""