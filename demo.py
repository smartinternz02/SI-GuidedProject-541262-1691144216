from flask import Flask,url_for,redirect
app=Flask(__name__)
@app.route('/home')
def home():
    return 'welcome All'

@app.route('/hello')
def hello():
    return 'Hello....All... Faculty'

@app.route('/hi')
def hi():
    return 'Hi.. All'
@app.route('/')
def index():
    return 'Index Page'
#http://localhost:5000/user/hello
#http://localhost:5000/user/hi
#http://localhost:5000/user/welcome
@app.route("/user/<enter>")
def user(enter):
    if enter=="welcome":
        return redirect(url_for("home"))
    elif enter=="hello":
        return redirect(url_for("hello"))
    elif enter=="hi":
        return redirect(url_for("hi"))

if __name__== "__main__":
    app.run(debug=True)