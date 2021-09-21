from flask import Flask 
from flask import render_template 
import sqlite3

conn = sqlite3.connect('sqlite_test.db') 
c = conn.cursor()
app = Flask(__name__)

@app.route('/') 
def index():    
 data = c.execute('SELECT * FROM tablename')    
 return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()



