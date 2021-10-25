import mysql.connector
import pandas as pd
import sqlalchemy
mydatabase = mysql.connector.connect(host="localhost", user = 'root', passwd= '12345', database=  'bigdataanalysis')
mycursor = mydatabase.cursor()
mycursor.execute('select * from covid19_details where country="India"')
getdata = mycursor.fetchall()
mydatabase.commit()
mydatabase.close()

totalDeath = 0
totalConfirmedCases = 0
totalRecoveredCases = 0
df = pd.DataFrame(getdata, columns =["Date", "Country", "Confirmed", "Recovered", "Deaths"])
df = df.sort_values(by="Date")
primeDate = 24

primeMonth = 3
i=0
primeYear = 2020
newDate = None
print(' Before lockdown: \n')
for row in df.itertuples():
	i+=1
	data = str(row[1])
	date = int(data[0:2])
	month = int(data[3:5])

	year = int(data[6:])
	if ( date <= primeDate and month <=primeMonth and year <= primeYear ) :
		totalDate = (str(date)+str(month)+str(year))
		if totalDate != newDate:
			totalDate = newDate
			totalDeath += row[5]
			totalConfirmedCases += row[3]
			totalRecoveredCases += row[4]
	else:
		pass
print('totalDeath is {} totalConfirmed is {} totalrecovered is {}'.format(totalDeath,totalConfirmedCases,totalRecoveredCases))

totalRecoveredCases = 0
totalConfirmedCases = 0
totalDeath = 0
print('\n In 2020 after lockdown: \n')

for row in df.itertuples():
	i+=1
	data = str(row[1])
	date = int(data[0:2])
	month = int(data[3:5])

	year = int(data[6:])
	if ( date <= 31 and month <= 12 and year == 2020 ) :
		totalDate = (str(date)+str(month)+str(year))
		if totalDate != newDate:
			totalDate = newDate
			totalDeath += row[5]
			totalConfirmedCases += row[3]
			totalRecoveredCases += row[4]
	else:
		pass
print('totalDeath is {} totalConfirmed is {} totalrecovered is {}'.format(totalDeath,totalConfirmedCases,totalRecoveredCases))

totalRecoveredCases = 0
totalConfirmedCases = 0
totalDeath = 0
print('\n In 2021 \n')
for row in df.itertuples():
	i+=1
	data = str(row[1])
	date = int(data[0:2])
	month = int(data[3:5])

	year = int(data[6:])
	if (  year == 2021 ) :
		totalDate = (str(date)+str(month)+str(year))
		if totalDate != newDate:
			totalDate = newDate
			totalDeath += row[5]
			totalConfirmedCases += row[3]
			totalRecoveredCases += row[4]
	else:
		pass
print('totalDeath is {} totalConfirmed is {} totalrecovered is {}'.format(totalDeath,totalConfirmedCases,totalRecoveredCases))

totalRecoveredCases = 0
totalConfirmedCases = 0
totalDeath = 0
print('\n Till Date \n')
for row in df.itertuples():
	i+=1
	data = str(row[1])
	date = int(data[0:2])
	month = int(data[3:5])

	year = int(data[6:])
	if ( date >= 1 and month >= 1 and year >= 2020 ) :
		totalDate = (str(date)+str(month)+str(year))
		if totalDate != newDate:
			totalDate = newDate
			totalDeath += row[5]
			totalConfirmedCases += row[3]
			totalRecoveredCases += row[4]
	else:
		pass
print('totalDeath is {} totalConfirmed is {} totalrecovered is {}'.format(totalDeath,totalConfirmedCases,totalRecoveredCases))
