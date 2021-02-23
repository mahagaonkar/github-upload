import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "mynameisyash",
    database = "status_check_test"
)

cursor = mydb.cursor()

cursor.execute("SELECT status FROM statuscheck")

status = cursor.fetchone()

print(status[0])