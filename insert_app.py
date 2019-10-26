from flask import Flask, render_template, request
from pyodbc import connect

conn = connect( 'Driver={SQL Server};'
                'Server=DESKTOP-KNDBAK9\SQLEXPRESS;'
                'Database=Lewis;'
                'Trusted_Connection=yes;' )

app = Flask(__name__)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        details = request.form
        id = details['fid']
        name = details['fname']
        model = details['fmodel']
        year = details['fyear']
        cur = conn.cursor()
        cur.execute('INSERT INTO Cars (Id, car_name, model, year_release) VALUES (?, ?, ?, ?)', id, name, model, year)
        cur.commit()
        cur.close()
        return render_template('success.htm')

    return render_template('index.htm')

if __name__ == '__main__':
    app.run(port='5000')