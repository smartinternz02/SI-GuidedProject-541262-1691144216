from flask import Flask
app = Flask(__name__)

@app.route('/blog/<postID>')
def show_blog(postID):
    s='Blog Number is : '+postID
    return s

@app.route('/rev/<revNo>')
def revision(revNo):
    rn='Revision Number '+revNo
    return rn

if __name__ == '__main__':
    app.run()

# say the URL is http://localhost:5000/blog/555
# say the URL is http://localhost:5000/rev/123
