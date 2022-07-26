# Create a common function to get database connection
import mysql.connector
def customer_db_details():
    con=mysql.connector.connect(user='root',password='Dhanu@1998',host='localhost',database='python_community',port=3306)
    return con
