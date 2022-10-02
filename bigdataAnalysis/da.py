# import pandas as pd
# tableData = pd.read_csv("./covid-data.csv", index_col=False, delimiter=',')
# print(tableData)
# for i, row in tableData.iterrows():
# 	sqlEntry = "insert into covid19_details values (%s,%s,%s,%s,%s)"
# 	mycursor.execute(sqlEntry,tuple(row))
# mycursor.execute('create database bigdataanalysis')
# mycursor.execute('create table covid19_details(date1 varchar(15) not null, country varchar(35) not null, confirmed_cases int, recovered_cases int, decreased_cases int, Primary key(date1, country))')
# mycursor.execute('load covid-data.csv local infile')
