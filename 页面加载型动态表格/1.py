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
@app.route("/add",methods=['GET','POST'])
def add():
    return render_template("add.html")
@app.route("/addCon",methods=['GET'])
def addCon():
    name=request.args.get("name")
    age= request.args.get("age")
    sex = request.args.get("sex")
    cursor = db.cursor()
    sql="insert into demo(name,age,sex) values('"+name+"','"+age+"','"+sex+"')"
    cursor.execute(sql)
    db.commit()
    arr=["添加完成","/add"]
    return render_template("finish.html",arr=arr)
@app.route("/dels",methods=['GET'])
def delete():
    cursor =db.cursor()
    id=request.args.get("id")
    sql="delete from demo where id ="+id
    cursor.execute(sql)
    db.commit()
    arr = ["删除完成", "/"]
    return render_template("finish.html",arr=arr)
@app.route("/edit",methods=['GET'])
def edit():
    id = request.args.get("id")
    cursor=db.cursor()
    sql="select * from demo where id="+id
    cursor.execute(sql)
    value=cursor.fetchone();
    return render_template("edit.html",value=value)
@app.route("/editorCon",methods=['GET'])
def editor():
    cursor =db.cursor()
    id = request.args.get("id")
    name=request.args.get("name")
    age = request.args.get("age")
    sex = request.args.get("sex")
    print(id,name,age,sex)
    sql="update demo set name='%s',age='%s',sex='%s' where id='%s'"%(name,age,sex,id)
    cursor.execute(sql)
    db.commit()
    arr=["编辑完成","/"]
    return render_template("finish.html",arr=arr)
app.debug=True;
app.run(host="0.0.0.0",port=7000)
