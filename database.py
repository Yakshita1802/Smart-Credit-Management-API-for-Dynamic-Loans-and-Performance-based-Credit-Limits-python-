import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host='localhost',
        user='b4137b7e',
        password='Cab#22se',
        database='b4137b7e',
        auth_plugin='mysql_native_password',
    )
    return db
