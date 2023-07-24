import sys
import mysql.connector
from mysql.connector import Error 

def createDB():
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="ved04")
    mycursor=mydb.cursor()
    mycursor.execute("create database if not exists VehiclesDB")
    mydb.commit()
    mycursor.close()
    mydb.close()

    
def createTable():
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="ved04", database="VehiclesDB")
    mycursor=mydb.cursor()
    mycursor.execute("create table VehiclesTB(\
                 VehicleNo int primary key,\
                 VehicleCompany varchar(50),\
                 NoWheels int)")
    mycursor.close()
    mydb.close()


def VehicleNoSearch():
    mydb=mysql.connector.connect(host="localhost", user='root',\
                            passwd='ved04', database='VehiclesDB')
    cursor=mydb.cursor()
    No=int(input("\nEnter Vehicle No to search: "))
    sql="select * from VehiclesTB where VehicleNo={}".format(No)
    cursor.execute(sql)
    row=0
    for row in cursor:
        print(row)
    if row==0:
        print("\nNot found")
    cursor.close()
    mydb.close()


def VehComSearch():
    mydb=mysql.connector.connect(host="localhost", user='root',\
                            passwd='ved04', database='VehiclesDB')
    cursor=mydb.cursor()
    VC=input("\nEnter Company to search: ")
    sql="select * from VehiclesTB where VehicleCompany='{}'".format(VC)
    cursor.execute(sql)
    data=cursor.fetchall()
    row=0
    for row in data:
        print(row)
    if row==0:
        print("\nNot found")
    cursor.close()
    mydb.close()

def NoWSearch():
    mydb=mysql.connector.connect(host="localhost", user='root',\
                            passwd='ved04', database='VehiclesDB')
    cursor=mydb.cursor()
    No=int(input("\nEnter No. of wheels to search: "))
    sql="select * from VehiclesTB where NoWheels={}".format(No)
    cursor.execute(sql)
    data=cursor.fetchall()
    row=0
    for row in data:
        print(row)
    if row==0:
        print("\nNot found")
    cursor.close()
    mydb.close()


def Insert():
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="ved04", database="VehiclesDB")
    cursor=mydb.cursor()
    print("Enter details: \n")
    vehno=int(input("Vehicle No: "))
    vehcom=input("Vehicle Company: ")
    noveh=input("No. of Wheels: ")
    sql="insert into VehiclesTB values\
    ({},'{}',{})".format(vehno, vehcom, noveh)
    cursor.execute(sql)
    mydb.commit()
    cursor.close()
    mydb.close()


def Delete():
    mydb=mysql.connector.connect(host="localhost", user='root', passwd='ved04', database='VehiclesDB')
    cursor=mydb.cursor()
    print("Enter Details: \n")
    A=int(input("Enter Vehicle No to delete: "))
    sql="select * from VehiclesTB where VehicleNo={}".format(A)
    cursor.execute(sql)
    row=0
    for row in cursor:
        print("Record to be deleted: \n")
        print(row)
        sql="delete from VehiclesTB where VehicleNo={}".format(A)
        cursor.execute(sql)
        print("\nRecord successfully deleted")
    if row==0:
        print("\nNot found")
    mydb.commit()
    cursor.close()
    mydb.close()


def Modify():
    mydb=mysql.connector.connect(host="localhost", user='root', passwd='ved04', database='VehiclesDB')
    cursor=mydb.cursor()
    print("Enter Details: \n")
    A=int(input("Enter Vehicle No to update record: "))
    sql="select * from VehiclesTB where VehicleNo={}".format(A)
    cursor.execute(sql)
    row=0
    for row in cursor:
        print("Record to be deleted: \n")
        print(row)
        com=input("\nEnter correct Company name: ")
        wheels=int(input("Enter Correct no. of wheels: "))
        sql="update VehiclesTB set VehicleCompany='{}', NoWheels={} where VehicleNo={}".format(com,wheels,A)
        cursor.execute(sql)
        print("\nRecord successfully Updated")
    if row==0:
        print("\nNot found")
    mydb.commit()
    cursor.close()
    mydb.close()


def Display():
    try:
        db = mysql.connector.connect(host='localhost',\
                database='VehiclesDB', user='root', password='ved04')
        if db.is_connected():
            print("Connected to MySQL database \n")
    except Error as e:
    	print(e)
    	return
    	#sys.exit() ->to kill program execution
    print("Records: \n")
    pysql=db.cursor()
    pysql.execute("select * from VehiclesTB")
    data=pysql.fetchall()
    for row in data:
    	print(row)
    pysql.close()
    db.close()

def permanent():
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="ved04", database="VehiclesDB")
    cursor=mydb.cursor()
    vehno1=12345
    vehcom1="Hyundai"
    noveh1=4
    vehno2=67890
    vehcom2="Honda"
    noveh2=2
    sql="insert into VehiclesTB values\
    ({},'{}',{})".format(vehno1, vehcom1, noveh1)
    cursor.execute(sql)
    sql="insert into VehiclesTB values\
    ({},'{}',{})".format(vehno2, vehcom2, noveh2)
    cursor.execute(sql)
    mydb.commit()
    cursor.close()
    mydb.close()


createDB()
createTable()
print("2 entries are already done to use various menu of the program")
permanent()
choice=1
while choice!=6:
    print("\nChoose any one:- \n")
    print("1. Search Record")
    print("2. Insert New Record")
    print("3. Delete Record")
    print("4. Modify Record")
    print("5. Display")
    print("6. Exit")
    choice=int(input("\nEnter your choice:- \n"))
    if choice==1:
        print("SEARCH PROCESS STARTS NOW:- \n")
        print('1. Search by Vehicle No\n')
        print('2. Search by Vehicle Company\n')
        print('3. Search by No. of Wheels\n')
        op=int(input('\n Enter your choice:-'))
        if op==1:
            VehicleNoSearch()
        elif op==2:
            VehComSearch()
        elif op==3:
            NoWSearch()
        else:
            print('Invalid option entered')
    elif choice==2:
        Insert()
    elif choice==3:
        Delete()
    elif choice==4:
        Modify()
    elif choice==5:
        Display()
    else:
        print("\nEnd of PROJECT\nThank you\n         Credits:\n         Vedang")
