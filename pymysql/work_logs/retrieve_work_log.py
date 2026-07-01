from  mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    database="trainer_log_db",
    host="localhost"
)



cursor = connection.cursor()

query = "select * from work_logs where id = %s"

cursor.execute(query,(2,))

record = cursor.fetchone()

print(record)

