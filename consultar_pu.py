import MySQLdb

mydb = MySQLdb.connect(host='',
    user='',
    passwd='',
    db='')
cursor = mydb.cursor()
PU = input("Ingrese pickup : " )
cursor.execute("""select * from sku where pu = %s""",(PU,))
resultado = cursor.fetchall()
for row in resultado :
    print("Modelo : ",row[0])
    print("Serial :", row[1])
    print("PU :", row[2])
#close the connection to the database.
#mydb.commit()
cursor.close()

