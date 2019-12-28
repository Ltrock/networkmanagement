from flask import Flask, render_template
import sqlite3 as sql
def convertfile():

    for y in range(4):   # number of files
        f=open("out"+str(y+1)+".txt","r")    
        fname = f.name.replace('.txt','')
        conn = sql.connect('data/'+fname+'.db') 
        conn.execute('CREATE TABLE outtable (oids TEXT, ka TEXT, types TEXT, times TEXT)')
        conn.close
        for x in range(150):    # row in a file
            
            t=f.readline().split('/')
            
            print(fname+" "+t[0])
            with sql.connect('data/'+fname+".db") as con:        
                    
                cur = con.cursor()
                cur.execute("INSERT INTO outtable (oids,ka,types,times) VALUES (?,?,?,?)",(t[1],t[0],t[2],t[3]) )
                con.commit()
        f.close
convertfile()