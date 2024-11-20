import mysql.connector
database = mysql.connector.connect(
    
    host="127.0.0.1",
    port=3305,
    user="root",
    passwd ="RaYudu902173@job"
)

cursorobject = database.cursor()
cursorobject.execute("create database Rayudu")
database.close()
print("database createdsuccessfully")
