from flask import Flask, render_template
import sqlite3 as sql
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')

@app.route('/router/')

def router():
    con = sql.connect('data/'+'system1'+'.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from snmp")
    sysrows = cur.fetchall()

    conn = sql.connect('data/'+'in2'+'.db')
    conn.row_factory = sql.Row
    curr = conn.cursor()
    curr.execute("select * from snmpin")
    udpinrows = curr.fetchall()

    connn = sql.connect('data/'+'out2'+'.db')
    connn.row_factory = sql.Row
    currr = connn.cursor()
    currr.execute("select * from outtable")
    udpoutrows = currr.fetchall()

    return render_template('router.html', sysrow=sysrows,udpinrow=udpinrows,udpoutrow=udpoutrows)

@app.route('/router2/')

def router2():
    con = sql.connect('data/'+'system3'+'.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from snmp")
    sysrows = cur.fetchall(); 

    conn = sql.connect('data/'+'in3'+'.db')
    conn.row_factory = sql.Row
    curr = conn.cursor()
    curr.execute("select * from snmpin")
    udpinrows = curr.fetchall()

    connn = sql.connect('data/'+'out3'+'.db')
    connn.row_factory = sql.Row
    currr = connn.cursor()
    currr.execute("select * from outtable")
    udpoutrows = currr.fetchall()

    return render_template('router2.html', sysrow=sysrows,udpinrow=udpinrows,udpoutrow=udpoutrows)

@app.route('/L2switch/')

def L2switch():
    con = sql.connect('data/'+'system2'+'.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from snmp")
    sysrows = cur.fetchall(); 

    conn = sql.connect('data/'+'in4'+'.db')
    conn.row_factory = sql.Row
    curr = conn.cursor()
    curr.execute("select * from snmpin")
    udpinrows = curr.fetchall()

    connn = sql.connect('data/'+'out4'+'.db')
    connn.row_factory = sql.Row
    currr = connn.cursor()
    currr.execute("select * from outtable")
    udpoutrows = currr.fetchall()

    return render_template('L2switch.html',sysrow=sysrows,udpinrow=udpinrows,udpoutrow=udpoutrows)

@app.route('/L3switch/')

def L3switch():
    con = sql.connect('data/'+'system4'+'.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from snmp")
    sysrows = cur.fetchall(); 

    conn = sql.connect('data/'+'in1'+'.db')
    conn.row_factory = sql.Row
    curr = conn.cursor()
    curr.execute("select * from snmpin")
    udpinrows = curr.fetchall()

    connn = sql.connect('data/'+'out1'+'.db')
    connn.row_factory = sql.Row
    currr = connn.cursor()
    currr.execute("select * from outtable")
    udpoutrows = currr.fetchall()

    return render_template('L3switch.html',sysrow=sysrows,udpinrow=udpinrows,udpoutrow=udpoutrows)

@app.route('/member/')

def member():

    return render_template('member.html')

if __name__ == '__main__':

    app.run(debug=True)