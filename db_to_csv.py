# Export database table data to csv/xlsx file
import mysql.connector
import csv
from customer_db_connect_fun import *
try:
    con=customer_db_details()
    cursor = con.cursor()
    query_string=("select * from tbl_customer_info;")
    cursor.execute(query_string)
    data=cursor.fetchall()
    print("data of tbl_customer_tbl_info:",data)
    with open('customer.csv','w',newline='') as csv_file:
        csv_writer= csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(data)
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem in sql:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()



