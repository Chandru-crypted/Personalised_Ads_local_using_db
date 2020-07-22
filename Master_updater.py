import sqlite3
from Updater import run_updater

print("\t \t \t \t Update your spendings here _|_ \t \t \t \t")

dict = {}

date = str(input("Enter the date in YY-mm-dd format : "))
dict["DATE"] = date

db_loc = r'C:\Users\chand\Documents\P\Projects\Locally_personalised_ads\db\payment_db.db'
table_name_1 = "tab1"

# Getting the last row from the db
command = "SELECT * FROM {} ".format(table_name_1) 
command += "ORDER BY ID "
command += "DESC LIMIT 1 ;"
conn = sqlite3.connect(db_loc)
curser = conn.execute(command)
names = [description[0] for description in curser.description]
for col in names[2:] :
	print()
	dict[col] = float(input("Enter how much did you spend in {} category : ".format(col)))
conn.close()

for col in dict.keys():
	print()
	print("You have entered {} for {}".format(dict[col], col))

print("\t \t \t \t Updating -|- \t \t \t \t")

run_updater(dict)