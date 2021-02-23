import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "mynameisyash",
    database = "status_check_test"
)

cursor = mydb.cursor()

#cursor.execute("CREATE DATABASE status_check_test")

#cursor.execute("CREATE TABLE statuscheck (status VARCHAR(255))")

#statusValue = "INSERT INTO statuscheck (status) VALUES (%s)"
#status_offline = ("offline", )
#cursor.execute(statusValue, status_offline)
#mydb.commit()

statusUpdate = "UPDATE statuscheck SET status = %s WHERE status = %s"
status_online_update = ("online", "offline")
cursor.execute(statusUpdate, status_online_update)
mydb.commit()

#statusUpdate = "UPDATE statuscheck SET status = %s WHERE status = %s"
#status_offline_update = ("offline", "online")
#cursor.execute(statusUpdate, status_offline_update)
#mydb.commit()

while True:
    command = input("Enter 'exit' to exit :")
    if command == 'exit':
        statusUpdate = "UPDATE statuscheck SET status = %s WHERE status = %s"
        status_offline_update = ("offline", "online")
        cursor.execute(statusUpdate, status_offline_update)
        mydb.commit()
        break