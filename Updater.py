'''
Requirements : 
The updater script will be called 
	1) Modify the date and the update the values after adding with the present value it got
	2) Then it checks whether the current date given for updation is the last of the month and calls the model

'''

#import 
import sqlite3 
from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar
import Model
import Compare

def checking_connection(db_loc):
	#establishing a connection 
	conn = sqlite3.connect(db_loc)
	conn.close()
	return (True)

def executing_command(command, db_loc):
	if checking_connection(db_loc):
		conn = sqlite3.connect(db_loc)
		conn.execute(command)
		conn.commit()
		conn.close()

def create_insert_command(table_name, dict_col_and_values):
	command = "INSERT INTO {} ".format(table_name)
	command += " ("
	for col in dict_col_and_values.keys():
		command += str(col) + str(" ,")
	command = command[: -1]
	command += ") "
	command += "VALUES" 
	command += "("	
	for col in dict_col_and_values.keys():
		command += str(dict_col_and_values[col]) + str(" ,")
	command = command[: -1]
	command += ")"
	command += ";"
	return command

def conv_day_into_month(day):
	day = datetime.strptime(day, "%Y-%m-%d")
	month = str(day.strftime("%Y-%m"))
	return (month)

def checking_whether_it_is_end_of_month(day):
	day = datetime.strptime(day, "%Y-%m-%d")
	last_day_of_month = calendar.monthrange(day.year, day.month)[1]
	if (last_day_of_month == day.day):
		return (True)
	return (False)


def run_updater(dict_col_values):
	print("Running updater -- ")
	db_loc = r'C:\Users\chand\Documents\P\Projects\Locally_personalised_ads\db\payment_db.db'
	table_name_1 = "tab1"

	# Getting the last row from the db
	command = "SELECT * FROM {} ".format(table_name_1) 
	command += "ORDER BY ID "
	command += "DESC LIMIT 1 ;"
	conn = sqlite3.connect(db_loc)
	curser = conn.execute(command)
	names = [description[0] for description in curser.description]
	data_tuple = []
	for row in curser:
		data_tuple = list(row)
	#print(data_tuple)

	prev_dict_col_values = {}
	i = 0
	for col in names:
		prev_dict_col_values[col] = data_tuple[i]
		i += 1
	#print(prev_dict_col_values)
	# Converting the date into month 
	day = dict_col_values["DATE"]
	month = conv_day_into_month(day)

	# Making the dict_col_values for insert command
	if (month == prev_dict_col_values["MONTH"]):
		for col in dict_col_values:
			if col in prev_dict_col_values.keys():
				dict_col_values[col] += prev_dict_col_values[col]
		del dict_col_values["DATE"]
		dict_col_values["MONTH"] = str('\'') + str(month) + str('\'')
		command = "DELETE FROM {} ".format(table_name_1)
		command += "WHERE ID = {}".format(prev_dict_col_values["ID"])
		#print(command)
		executing_command(command, db_loc)
		dict_col_values["ID"] = prev_dict_col_values["ID"]

	elif (month != prev_dict_col_values["MONTH"]):
		del dict_col_values["DATE"]
		dict_col_values["MONTH"] = str('\'') + str(month) + str('\'')

	print("Inserting the data  -- in tab1")
	command = create_insert_command(table_name_1, dict_col_values)
	#print(command)
	executing_command(command, db_loc)
	#print("in dict ", dict_col_values)

	Compare.run_compare()

	#Checking whether it is last day of the month
	if (checking_whether_it_is_end_of_month(day)):
		Model.run_model()


if __name__ == "__main__":
	dict_col_values = {"DATE" : "2018-12-31", 
						"FOOD" : 100,
						"FUEL" : 40
					}	
	run_updater(dict_col_values)

#48	2018-12	9200	1250


# UPDATE tab1
# SET MONTH = "2018-12",
# FOOD = 1900,
# FUEL= 500
# WHERE ID = 55;