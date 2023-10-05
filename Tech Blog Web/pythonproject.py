from flask import Flask, render_template, request, make_response
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'techblog'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Community')
def contact():
    return render_template('Community.html')

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