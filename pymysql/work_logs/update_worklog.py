from  mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    database="trainer_log_db",
    host="localhost"
)



cursor = connection.cursor()

query = "update  work_logs set batch = %s where id = %s"

values=("PYTHON DJANGO APRIL",2)


cursor.execute(query,values)

connection.commit()

print("record inserted")