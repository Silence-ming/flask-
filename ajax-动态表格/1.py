from flask import Flask,render_template,request
import json
import pymysql
import time
app=Flask(__name__)
db=pymysql.connect("localhost","root","root","u1801",charset='utf8')
@app.route("/",methods=["GET"])
def a():
    return render_template("index.html")
@app.route("/select",methods=["GET"])
def select():
    time.sleep(1)  #延迟两秒
    cursor=db.cursor()
    sql="select * from demo"
    cursor.execute(sql)
    result=json.dumps(cursor.fetchall()) #转化为json格式
    return result
@app.route("/add",methods=["POST"])
def add():
    cursor=db.cursor()
    sql = "insert into demo(name,age,sex) values('','','')"
    cursor.execute(sql)
    id = (db.insert_id())  #获取最后一次插入的id值
    db.commit()
    return str(id)
@app.route("/del",methods=["POST"])
def dels():
    cursor=db.cursor()
    id=request.form["id"]
    sql="delete from demo where id=%s"%(id)
    cursor.execute(sql)
    db.commit()
    return "ok"
@app.route('/edit',methods=["POST"])
def edit():
    id=request.form["id"]
    name=request.form["className"]
    value=request.form["value"]
    cursor=db.cursor()
    sql="update demo set %s='%s' where id=%s"%(name,value,id)
    cursor.execute(sql)
    db.commit()
    return "ok"
app.run(host='0.0.0.0',port=2000)