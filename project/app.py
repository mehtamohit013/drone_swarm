from flask import Flask, render_template, request, url_for, send_file, session, redirect ,escape
import os
import mysql.connector

app = Flask(__name__)

#Receiving the data from rpi to the lapop

@app.route('/',methods=['GET','POST'])
def datareceiver():

	if(request.method == 'POST'):

		print("Writing data to the database ...............")

		lat="{0:.8f}".format(request.form['Latitude'])
		lon="{0:.8f}".format(request.form['Longitude'])
		tar=int(request.form['Target_Detected'])

		print("Received data: ",lat," ",lon," ",tar)

		if(tar>0):

			print("Target detected is non-zero. ")

			mydb=mysql.connector.connect(host="localhost", user="mohit", password="passwd", database="DroneData")
			mycursor=mydb.cursor()

			query="INSERT INTO data VALUES(%f,%f,%d)"
			val=(lat,lon,tar)

			mycursor.execute(query,val)
			mycursor.commit()
			mydb.commmit()
			print("Data successfully send to Laptop. ",mycursor.rowcount, " record inserted")

			mycursor.close()
			mydb.close()

			return render_template('home.html',lat=lat,lon=lon,tar=tar)

		else:	

			lat=0
			lon=0
			tar=0
			print("Target Detected is zero. Please try again")

	else:
		lat=0
		lon=0
		tar=0
		print("Data not received.")

	return render_template('yeah.html')


#Displaying the data received from mysql
@app.route('/dronedata',methods=['GET','POST'])
def showdata():
	mydb=mysql.connector.connect(host="localhost", user="mohit", password="passwd", database="DroneData")
	mycursor=mydb.cursor()

	mycursor.execute("SELECT*FROM data")
	data = mycursor.fetchall()
	print(data)

	mycursor.close()
	mydb.close()

	return render_template('dronedata.html',data=data)


@app.route('/yeah', methods=['GET', 'POST'])
def yeah():
	return render_template('yeah.html')
	

if __name__=='__main__':
	app.run(host='0.0.0.0' , port=8000, debug=True)
	
