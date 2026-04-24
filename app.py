from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            checkin TEXT,
            checkout TEXT,
            room_type TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        name = request.form['name']
        checkin = request.form['checkin']
        checkout = request.form['checkout']
        room_type = request.form['room_type']

        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO reservations (name, checkin, checkout, room_type)
            VALUES (?, ?, ?, ?)
        ''', (name, checkin, checkout, room_type))

        conn.commit()
        conn.close()

        return render_template(
            'confirmation_page.html',
            name=name,
            checkin=checkin,
            checkout=checkout,
            room_type=room_type
        )

    return render_template('reservation.html')

@app.route('/room-list')
def room_list():
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM reservations')
    reservations = cursor.fetchall()

    conn.close()

    return render_template('room_list.html', reservations=reservations)

if __name__ == '__main__':
    app.run(debug=True)
