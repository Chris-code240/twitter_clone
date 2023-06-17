from models import app
from flask import render_template, request,redirect,jsonify

@app.route('/')
def render_login():
    return render_template('login.html')
@app.route('/login')
def get_login():
    return redirect('/')

@app.route('/sign-up')
def get_signup():
    return render_template('signup.html')
@app.route('/feed')
def feed():
    return render_template('feed.html')
@app.route('/login',methods=['POST'])
def login():
    """Implement login logic"""
    return render_template('feed.html')



if __name__ == "__main__":
    app.run(debug=True)