from flask import Flask,url_for,render_template,request
import ibm_db
app=Flask(__name__)
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;UID=syw86972;PASSWORD=3kX4WUt1esKO7Ocy;SECURITY=ssl;SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt","","")
print(ibm_db.active(conn))
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        un=request.form.get('username')
        ps=request.form.get('password')
        name=request.form.get('name')
        email=request.form.get('email')
        roll=request.form.get('roll')
        sql='INSERT INTO REGISTER VALUES(?,?,?,?,?)'
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,name)
        ibm_db.bind_param(stmt,2,un)
        ibm_db.bind_param(stmt,3,ps)
        ibm_db.bind_param(stmt,4,email)
        ibm_db.bind_param(stmt,5,roll)
        data=ibm_db.execute(stmt)
        print("Data Registration success ",data)
        
        
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        un=request.form.get('username')
        ps=request.form.get('password')
        sql='SELECT * FROM REGISTER WHERE USERNAME=?  AND PASSWORD=?'
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,un)
        ibm_db.bind_param(stmt,2,ps)
        ibm_db.execute(stmt)
        data=ibm_db.fetch_assoc(stmt)
        print("Data From Database",data)
        print(data)
        if data==False:
            msg="Invalid UserName or Password"
            return render_template('login.html',login_message=msg)
        else:
            role=data['ROLL']
            name=data['NAME']
            print("Role is : ",role)
            if role==0:
                return render_template("adminprofile.html",msg=name)
            elif role==1:
                return render_template("facultyprofile.html",msg=name)
            elif role==2:
                return render_template("studentprofile.html",msg=name)
    return render_template('login.html')
    
@app.route('/fetch', methods=['GET'])
def fetch():
    if request.method=='GET':
        sql='SELECT * FROM REGISTER'
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.execute(stmt)
        data=ibm_db.fetch_both(stmt)
        print("Data From Database",data)
        d_list = {}
        while data != False:
            print (": ", data["NAME"],'  ',data['EMAIL'],'  ',data['USERNAME'],'  ',data['ROLL'])
            d_list.append(data)
            data = ibm_db.fetch_both(stmt)
            print(data)
            
        l = len(d_list)
        print(l)
        
    return render_template('view.html',l = l, info = data)
    


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__== "__main__":
    app.run(debug=True)
