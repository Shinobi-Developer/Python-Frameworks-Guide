from flask import Flask, request
import pymysql

def create_app():
    app = Flask(__name__)
    
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'flask'
    
    mysql = pymysql.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'], password=app.config['MYSQL_PASSWORD'], db=app.config['MYSQL_DB'])
    
    cursor = mysql.cursor()
    
    @app.route('/insert', methods=['POST'])
    def insert():
        if request.method == 'POST':
            name = request.form['name']
            gender = request.form['gender']
            birthday = request.form['birthday']
            print(name, gender, birthday)
            cursor.execute("INSERT INTO users  (name, gender, birthday) VALUES (%s, %s, %s)", [name, gender, birthday])
            mysql.commit()
            cursor.close()
            return 'Success'
            
    return app