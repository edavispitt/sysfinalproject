from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def welcome():
   return render_template('welcome.htm')

@app.route('/newreservation')
def new_reservation():
   return render_template('reservation.htm')

@app.route('/addreservation',methods = ['POST', 'GET'])
def add_reservation():
   if request.method == 'POST':
      try:
         name = request.form['nm']
         checkin = request.form['chkin']
         checkout = request.form['chkout']
         roomtype = request.form['rm']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO reservations (name,checkin,checkout,roomtype) VALUES ('{0}','{1}','{2}','{3}')".format(name,checkin,checkout,roomtype))
            
            con.commit()
            msg = ("{0}, your Reservation has been scheduled from {1} to {2}. Thank you, and see you soon!").format(name,checkin,checkout)
      except:
         con.rollback()
         msg = "an error has occured while trying to submit your reservation."
      
      finally:
         return render_template("confirmation.htm",msg = msg)
         con.close()

@app.route('/reservationlist')
def reservation_list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from reservations")
   
   rows = cur.fetchall(); 
   return render_template("reservelist.htm",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)