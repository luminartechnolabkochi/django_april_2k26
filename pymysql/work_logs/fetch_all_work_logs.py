from  mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    database="trainer_log_db",
    host="localhost"
)

# print(connection)

# step2 crete cursor object


cursor = connection.cursor()

# step3 query

query = "select * from work_logs"

# step4 execute query

cursor.execute(query)

rows = cursor.fetchall()

print(rows)
