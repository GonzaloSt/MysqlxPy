import MySQLdb

mydb = MySQLdb.connect(host='35.237.244.166',
        user='gonza',
        passwd='1mecagoendios1',
        db='sku')
cursor = mydb.cursor()
modelo = input ( "Por favor,ingrese modelo de su maquina: " )
serial = input ( "Por favor,ingrese serial de su maquina: " )
pu = input( "Por favor,ingrese el pickup de su maquina: " )

agregar  = """INSERT INTO sku ( modelo , serial , pu ) VALUES ( %s ,%s ,%s )"""
datos = ( modelo , serial , pu )
cursor.execute( agregar ,datos )
resultado = cursor.fetchall()	

#close the connection to the database
mydb.commit()
cursor.close()

