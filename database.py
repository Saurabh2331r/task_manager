import mysql.connector
import mail

mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345@ab")

mycursor=mydb.cursor()
mycursor.execute("create database if not exists task_manager_data")
mycursor.execute("use task_manager_data")
def create_database(username):
    global email
    global name
    email=username
    ans=username.split("@")
    name=ans[0]
    print(name)
    query=f"CREATE TABLE IF NOT EXISTS {name}(Sno int,Title varchar(100),Category varchar(50),Priority varchar(15),Deadline varchar(50),Status varchar(20))"
    mycursor.execute(query)
    mydb.commit()
mycursor.execute("create table if not exists login_info(username varchar(70), password varchar(50))")
mydb.commit()






def fetch_tasks():
    mycursor.execute(f"select * from {name}")
    result=mycursor.fetchall()
    return result


def sno_count():
    mycursor.execute(f"select * from {name}")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    r=count+1
    return r


def insert(sno, title, category, priority, deadline, status):
    sql_query = f"INSERT INTO {name} (SNo, Title, Category, Priority, Deadline, Status) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (sno, title, category, priority, deadline, status)
    mycursor.execute(sql_query, values)
    mydb.commit()


def update(sno, title, category, priority, deadline, status):
    sql_query = f"UPDATE {name} SET Title = %s, Category = %s, Priority = %s, Deadline = %s, Status = %s WHERE SNo = %s"
    values = (title, category, priority, deadline, status, sno)
    mycursor.execute(sql_query, values)
    mydb.commit()

def delete(title):
    sql_query = f"DELETE FROM {name} WHERE Title = %s"
    values = (title,)
    mycursor.execute(sql_query, values)
    mydb.commit()
 

def search(option, value):
    sql_query = f"SELECT * FROM {name} WHERE {option} = %s"
    values = (value,)
    mycursor.execute(sql_query, values)
    result = mycursor.fetchall()
    return result


def login_check(username,password):
    mycursor.execute("select count(*) from login_info where username=%s and password=%s",(username,password))
    result=mycursor.fetchone()
    return result[0]>0

def mail_send():
    query=f"select * from {name} where status=\'pending\'"
    mycursor.execute(query)
    result=mycursor.fetchall()
    for i in result:
        if i[5]=='Pending':
            mail.send_mail(i,email)