from flask import Flask,render_template,request,json,jsonify,session
import sqlite3
import numpy as np
import random


import joblib
model = joblib.load("3045etc.sav")

db=sqlite3.connect("student.db")
db=db.execute('''CREATE TABLE IF NOT EXISTS student_table
                    (Name TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Gender TEXT NOT NULL,
                    English_Prof TEXT NOT NULL,
                    Java_Prof TEXT NOT NULL,
                    Python_Prof TEXT NOT NULL,
                    Machine_Learning_Prof TEXT NOT NULL,
                    Score INT DEFAULT -1,
                    pred_result TEXT DEFAULT NAN
                    )''')


db.close()
app=Flask(__name__)
app.secret_key="secure"
@app.route('/')
def first_page():
    return render_template("first_page.html")

@app.route('/form_page/', methods=["get"])
def form_page():
    return render_template("form_page.html")

@app.route('/form_update/',methods=["post"])
def form_update():
    data=json.loads(request.data)
    name=data["name"]
    email=data["email"]
    gender=data["gender"]
    eng=data["eng"]
    java=data["java"]
    python=data["python"]
    ml=data["ml"]
    db=sqlite3.connect("student.db")
    
    check_student=db.execute(f'''SELECT * FROM student_table
                       WHERE Name = "{name}" 
                       AND Email ="{email}";''').fetchall()
    print(check_student)
    if len(check_student)==0:
        db.execute(f'''INSERT INTO student_table 
                (Name,Email,Gender,English_Prof,Java_Prof, Python_Prof,
                Machine_Learning_Prof)
                VALUES ('{name}','{email}','{gender}','{eng}',
                '{java}', '{python}','{ml}');''')
        msg="success"
        session["student"]=name
        session["email"]=email
    
    elif len(check_student)!=0 and check_student[0][7]==-1:
    
        session["student"]=name
        session["email"]=email
        msg="success"
    else:
        session["student"]=name
        session["email"]=email
        msg="fail"
    db.commit()
    db.close() 
    return jsonify(dict(msg=msg))      
@app.route('/test_page/')
def test():
    db=sqlite3.connect("student.db")
    ques=db.execute(f"""SELECT Q_number,Question,Option_A,Option_B,
                    Option_C,Option_D FROM test_table
                    ORDER BY RANDOM()
                    LIMIT 10; """).fetchall()
   
    return render_template("test_page.html",questions=ques)

@app.route('/collect_answers/',methods=["post"])
def evaluation():
    data2=json.loads(request.data)
    ques_list=[]
    ans_list=[]
    for i in data2:
        ques_list.append(i[0:-1])
        ans_list.append(i[-1])
    que_ans=list(dict(zip(ques_list, ans_list)).items())
    result=0
    db=sqlite3.connect("student.db")
    for i in que_ans:
        record=db.execute(f'''SELECT * FROM test_table 
                          WHERE Q_number='{i[0]}' 
                          and Answer='{i[1]}'; ''').fetchall()
        if len(record)>0:
            result+=1
    
    user_data = db.execute(f'''SELECT * FROM student_table
                       WHERE Name = "{session["student"]}" 
                       AND Email ="{session['email']}";''').fetchall()
    user_data = user_data[0][2:len(user_data[0])-2]
    rep = {"Male":0,"Female":1,"Other":2,"Beginner":0,"Intermediate":1,"Advanced":2}
    target_uni = ["Data scientist","full-stack dev","tech-support","non-tech support","finance"]
    pred_in = []
    for i in user_data:
        pred_in.append(rep[i])
    pred_in = pred_in + [result]
    print(pred_in)
    pred_out = model.predict(np.array(pred_in).reshape(1,-1))[0]
    pred_out = target_uni[pred_out]

    db.execute(f'''UPDATE student_table SET Score={result},pred_result='{pred_out}' WHERE Name='{session["student"]}' AND Email='{session["email"]}';''')
    db.commit()
    db.close()

    return {"score":result,"fin_out":pred_out,"c1":" ","c2":" "}


@app.route("/stored_result/<score>/<fin_out>/<c1>/<c2>")
def result(score,fin_out,c1,c2):
    db=sqlite3.connect("student.db")
    r=db.execute(f'''SELECT score,pred_result FROM student_table 
                          WHERE Name='{session["student"]}' 
                          and Email='{session["email"]}'; ''').fetchall()[0]
    links = ["https://www.tcs.com/","https://www.infosys.com/","https://www.mphasis.com/","https://www.genpact.com/careers","https://www.nttdata.com/global/en/"]
    c1=random.choice(links)
    c2=random.choice(links)
    while c1==c2:
        c2=random.choice(links)
    return render_template('result.html', score=r[-2], fin_out=r[-1],c1=c1,c2=c2)

@app.route("/show_result/")
def show_res():
    db=sqlite3.connect("student.db")
    r=db.execute(f'''SELECT score,pred_result FROM student_table 
                          WHERE Name='{session["student"]}' 
                          and Email='{session["email"]}'; ''').fetchall()[0]
    links = ["https://www.tcs.com/","https://www.infosys.com/","https://www.mphasis.com/","https://www.genpact.com/careers","https://www.nttdata.com/global/en/"]
    c1=random.choice(links)
    c2=random.choice(links)
    while c1==c2:
        c2=random.choice(links)
    return render_template('result.html', score=r[-2], fin_out=r[-1],c1=c1,c2=c2)
    
app.run(debug=True)