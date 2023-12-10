"""
@author = hari
@email  = harihararajanrm.cms@gmail.com 
-----------------------------------------
Topics covered in this tutorial
- Integrate flask with html 
- return the content from a HTML file
- HTTP verb GET and POST methods
"""

from flask import Flask, redirect, url_for

from flask import Flask, redirect, url_for, request,render_template

#####
# NOTE: to ise reder_template - create a new folder named "templates" in the cwd
# with in templates folder create index.html file
# folder name should be templates
# pay attention to return statement of every function
#####

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') # PAY ATTENTION #

@app.route('/success/<int:score>')
def success(score:int): 
    if score >=50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', result =res, score=score)

@app.route('/results/<int:Marks>') 
def results(Marks):
    """
    for documentation refer -> tut_flask_01.py
    """
    
    result =""
    if Marks >= 50:
        result ="success"
    else:
        result ="fail"
    
    return redirect(url_for(result, score=Marks))

## Result checker html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science']) # 'science' should match with the 'name' in input field of html form 
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = science+maths+c+datascience
        average = total_score/4
        res = "success"
    return redirect(url_for(res, score=average))

if __name__ == '__main__':
    app.run(debug=True)