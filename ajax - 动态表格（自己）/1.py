from flask import Flask,render_template,request
import pymysql
db=pymysql.connect("localhost","root","root","u1801",charset='utf8')
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def aa():
    cursor = db.cursor()
    sql = "select * from demo"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("index.html",results=results)
@app.route("/add",methods=['GET'])
def add():
    cursor=db.cursor()
    sql="insert into demo(name,age,sex) values('','','')"
    cursor.execute(sql)
    db.commit()
    return "ok"
@app.route('/dels',methods=['GET'])
def dels():
    cursor=db.cursor()
    id=request.args.get("id")
    sql="delete from demo where id="+id
    cursor.execute(sql)
    db.commit()
    return "ok"
@app.route('/edit',methods=['POST'])
def edit():
    cursor=db.cursor()
    id=request.form["id"]
    val = request.form["val"]
    attr = request.form["attr"]
    sql = "update demo set %s='%s' where id=%s" % (attr, val, id)
    cursor.execute(sql)
    db.commit()
    return "ok"
app.debug=True;
app.run(host="0.0.0.0",port=1000)
