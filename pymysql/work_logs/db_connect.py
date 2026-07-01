from  mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    database="trainer_log_db",
    host="localhost"
)

print(connection)