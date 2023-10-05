from flask import Flask, redirect, render_template, Response, url_for,session, request, make_response
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='TECHBLOG'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/Community')
def contact():
    return render_template('Community.html')

@app.route('/index1', methods = ['POST'])
def index1():
    print('index1')
    try:
        if request.method == "POST":
            product_ID = request.form['product_ID']
            user_ID = request.form['user_ID']
            comment_In = request.form['comment_In']
            sysdate_column=request.form['sysdate_column']
            cur = mysql.connection.curser()
            
            cur.execute("INSERT INTO user3 (product_ID,user_ID,comment_In,sysdate_column) VALUES (%s,%s,%s,%s)")
            
            mysql.connection.commit()
            return redirect (url_for('index'))
            cur.close()
        return render_template('community.html')
    except:
        return render_template('Home.html')
    
if __name__ == '__main__':
   app.run(threaded=True)