import sqlite3

from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route('/data',methods=['GET'])
def get_user():
    con=sqlite3.connect('data.db')
    corsur=con.cursor()
    corsur.execute("INSERT INTO data(name,lastname,address,id,password), VALUES(?,?,?,?,?)",(name,lastname,address,id,password))
    con.commit()
    con.close()
    return jsonify(message="user created successfully")


