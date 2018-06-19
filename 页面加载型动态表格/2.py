from flask import Flask
import pymysql
app=Flask(__name__)
db=pymysql.connect("localhost","root","123456","u1801")
@app.route("/",methods=["GET"])
def aa():
   return "55"
app.run(host="0.0.0.0",port=1000)