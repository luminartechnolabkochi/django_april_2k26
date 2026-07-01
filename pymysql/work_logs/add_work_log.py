from  mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    database="trainer_log_db",
    host="localhost"
)



cursor = connection.cursor()

query = "insert into work_logs (batch,topic,trainer) values(%s,%s,%s)"

values=("pydjango april","python-mysql","sajay")


cursor.execute(query,values)

connection.commit()

print("record inserted")