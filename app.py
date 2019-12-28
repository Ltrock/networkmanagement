from flask import Flask, render_template
import sqlite3 as sql
#from flask_sqlalchemy import SQLAlchemy
#from graph import build_graph
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

app = Flask(__name__)

def build_graph(x_coordinates, y_coordinates):
    img = io.BytesIO()
    plt.plot(x_coordinates, y_coordinates)
    plt.ylabel('y - axis: Value')
    plt.xlabel('x - axis: Time (min:sec)')
    plt.title('UdpDatagram graph')
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

@app.route('/')

@app.route('/router/')

def router():
    
    con = sql.connect('data/'+'system1'+'.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from snmp")
    sysrows = cur.fetchall()
    
    y1 = [36055, 36070, 36086, 36102, 36118,36134,36151,36167,36185,36202]
    x1 = ["10:35","10:41","10:46","10:51","10:56","11:01","11:07","11:12","11:17","11:22"]
    graph1_url = build_graph(x1,y1)

    conn = sql.connect('data/'+'in2'+'.db')
    conn.row_factory = sql.Row
    curr = conn.cursor()
    curr.execute("select * from snmpin")
    udpinrows = curr.fetchall()

    y2 = [35796, 35812,35828,35844, 35860,35876,35892,35910,35927,35942]
    x2 = ["09:42","09:48","09:53", "09:58","10:03","10:08","10:13","10:19","10:24","10:29"]
    graph2_url = build_graph(x2,y2)

    connn = sql.connect('data/'+'out2'+'.db')
    connn.row_factory = sql.Row
    currr = connn.cursor()
    currr.execute("select * from outtable")
    udpoutrows = currr.fetchall()

    return render_template('router.html', sysrow=sysrows,graph1=graph1_url,udpinrow=udpinrows,graph2=graph2_url,udpoutrow=udpoutrows)

@app.route('/router2/')

def router2():
    con = sql.connect('data/'+'system3'+'.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from snmp")
    sysrows = cur.fetchall(); 
    y3 = [2660, 2677,2693,2709, 2724,2739,2755,2771,2787,2803]
    x3 = ["06:32","06:38","06:43", "06:48","06:53","06:58","07:03","07:08","07:13","07:18"]
    graph3_url = build_graph(x3,y3)

    conn = sql.connect('data/'+'in3'+'.db')
    conn.row_factory = sql.Row
    curr = conn.cursor()
    curr.execute("select * from snmpin")
    udpinrows = curr.fetchall()
    y4 = [2826, 2843,2859,2875, 2891,2907,2925,2942,2958,2974]
    x4 = ["08:02","08:07","08:13", "08:18","08:23","08:28","08:33","08:38","08:43","08:48"]
    graph4_url = build_graph(x4,y4)

    connn = sql.connect('data/'+'out3'+'.db')
    connn.row_factory = sql.Row
    currr = connn.cursor()
    currr.execute("select * from outtable")
    udpoutrows = currr.fetchall()

    return render_template('router2.html', sysrow=sysrows,graph3=graph3_url,graph4=graph4_url,udpinrow=udpinrows,udpoutrow=udpoutrows)

@app.route('/L2switch/')

def L2switch():
    con = sql.connect('data/'+'system2'+'.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from snmp")
    sysrows = cur.fetchall(); 
    y5 = [6038, 6054,6070,6088, 6103,6118,6133,6149,6165,6181]
    x5 = ["24:33","24:38","24:43", "24:48","24:54","24:59","25:04","25:09","25:14","25:19"]
    graph5_url = build_graph(x5,y5)

    conn = sql.connect('data/'+'in4'+'.db')
    conn.row_factory = sql.Row
    curr = conn.cursor()
    curr.execute("select * from snmpin")
    udpinrows = curr.fetchall()

    y6 = [6324, 6339,6354,6370, 6386,6403,6418,6434,6450,6467]
    x6 = ["28:54","28:59","29:05", "29:10","29:15","29:20","29:25","29:30","29:35","29:40"]
    graph6_url = build_graph(x6,y6)
    connn = sql.connect('data/'+'out4'+'.db')
    connn.row_factory = sql.Row
    currr = connn.cursor()
    currr.execute("select * from outtable")
    udpoutrows = currr.fetchall()

    return render_template('L2switch.html',sysrow=sysrows,graph5=graph5_url,graph6=graph6_url,udpinrow=udpinrows,udpoutrow=udpoutrows)

@app.route('/L3switch/')

def L3switch():
    con = sql.connect('data/'+'system4'+'.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from snmp")
    sysrows = cur.fetchall(); 

    y7 = [4330, 4345,4360,4375,4392,4408,4425,4442,4458,4475]
    x7 = ["04:49","04:54","04:59", "05:05","05:10","05:15","05:20","05:25","05:30","05:35"]
    graph7_url = build_graph(x7,y7)

    conn = sql.connect('data/'+'in1'+'.db')
    conn.row_factory = sql.Row
    curr = conn.cursor()
    curr.execute("select * from snmpin")
    udpinrows = curr.fetchall()

    y8 = [3449,3464,3480,3494,3509,3524,3539, 3554,4285,4300]
    x8 = ["02:27","02:32","02:37", "02:42","02:47","02:52","02:57","03:02","03:58","04:04"]
    graph8_url = build_graph(x8,y8)

    connn = sql.connect('data/'+'out1'+'.db')
    connn.row_factory = sql.Row
    currr = connn.cursor()
    currr.execute("select * from outtable")
    udpoutrows = currr.fetchall()

    return render_template('L3switch.html',sysrow=sysrows,graph7=graph7_url,graph8=graph8_url,udpinrow=udpinrows,udpoutrow=udpoutrows)

@app.route('/member/')

def member():

    return render_template('member.html')

if __name__ == '__main__':

    app.run(debug=True)