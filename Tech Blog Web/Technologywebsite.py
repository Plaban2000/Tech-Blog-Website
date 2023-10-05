from flask import Flask, redirect, render_template, Response, url_for,session, request, make_response
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='TECHBLOG'
''' Connecting Flask App with MySQL '''
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Home')
def home2():
    return render_template('Home.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/Community')
def contact():
    return render_template('Community.html')

@app.route('/login')  
def signin():
    return render_template("login.html") 

@app.route('/signup')  
def signup():
    return render_template("register.html") 

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/laptop')
def laptop():
    return render_template('laptop.html')

@app.route('/registration', methods = ['POST', 'GET'])
def registration():
    print('Registration')
    try:
        if request.method == 'POST':
           FName = request.form['FName']
           LName = request.form['LName']
           Email=request.form['Email']
           Password = request.form['Password']
           confirm_password=request.form['Password']
           print(FName,LName,Email,Password,confirm_password)
           resp = make_response(render_template('login.html'))
           resp.set_cookie('Email', Email)
           resp.set_cookie('Password',Password)
           cur = mysql.connection.cursor()
           if Password==confirm_password:
               sql = "INSERT INTO users (FName, LName, Email, Password) VALUES (%s,%s,%s,%s)"
               val = (FName, LName,Email,Password)
               cur.execute(sql, val)
               cur.close()
           return render_template('login.html')
    except:
        return render_template('register.html')
@app.route('/login', methods = ['POST', 'GET'])
def login(): 
    print("0")
    try:
        if request.method == 'POST':
           print("1")
           email=request.form['Email']   
           print("2")
           password = request.form['Password']
           print("3")
           print(email,password)
           resp = make_response(render_template('login.html'))
           resp.set_cookie('Email', email)
           resp.set_cookie('Password',password)
           cur = mysql.connection.cursor()
           sql = "SELECT * FROM users WHERE email=%s and password=%s"
           val = (email,password)
           cur.execute(sql, val)
           fetchdata=cur.fetchall()
           print(fetchdata)
           cur.close()
           if len(fetchdata)!=0:
               print("successful login")
               #session['email']=request.form['email']  
               return render_template('Home.html')
           return resp
    except Exception:
        print("login failed")
        return render_template('login.html')
    
@app.route('/index1', methods=['POST'])
def index1():
    try:
        if request.method == 'POST':
            product_ID = request.form['product_ID']
            user_ID = request.form['user_ID']
            comment_In = request.form['comment_In']
            #sysdate_column = request.form['sysdate_column']
            print(product_ID, user_ID, comment_In)
            print('values inserted')
            resp = make_response(render_template('community.html'))
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO user3 (product_ID, user_ID, comment_In) VALUES (%s, %s, %s)", (product_ID, user_ID, comment_In))
            mysql.connection.commit()  # Commit changes to the database
            cursor.close()
            return render_template('community.html')
    except Exception as e:
        print(e)
        return render_template('Home.html')
    
@app.route('/index2', methods=['GET'])
def index2():
    try:
        if request.method == 'GET':
            
            cursor = mysql.connection.cursor()
            sql = "SELECT * FROM user3"
            cursor.execute(sql)  # Commit changes to the database
            print(cursor.fetchall())
            cursor.close()
            return render_template('community.html')
    except Exception as e:
        print(e)
        return render_template('Home.html')
if __name__ == '__main__':
    app.run(threaded=True)