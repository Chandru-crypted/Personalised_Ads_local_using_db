import sqlite3 

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


def get_the_last_row(table_name,db_loc):
	conn = sqlite3.connect(db_loc)
	command = "SELECT count(*) FROM {}".format(table_name)
	curser = conn.execute(command)
	for row in curser:
		count = row[0]
	if (count > 0):
		command = "SELECT * FROM {} ".format(table_name) 
		command += "ORDER BY ID "
		command += "DESC LIMIT 1 ;"
		conn = sqlite3.connect(db_loc)
		curser = conn.execute(command)
		names = [description[0] for description in curser.description]
		data_tuple = []
		for row in curser:
			data_tuple = list(row)
		prev_dict_col_values = {}
		i = 0
		for col in names:
			prev_dict_col_values[col] = data_tuple[i]
			i += 1
		return (prev_dict_col_values)
	else:
		prev_dict_col_values = {}
		command = "SELECT * FROM {} ".format(table_name) 
		command += "ORDER BY ID "
		command += "DESC LIMIT 1 ;"
		conn = sqlite3.connect(db_loc)
		curser = conn.execute(command)
		names = [description[0] for description in curser.description]

		i = 0
		for col in names:
			prev_dict_col_values[col] = 0
			i += 1
		return(prev_dict_col_values)


def run_compare():
	print("Running the compare --")
	db_loc = r'C:\Users\chand\Documents\P\Projects\personalised_ads_with_flask\db\payment_db.db'
	table_name_1 = "tab1"
	table_name_2 = "tab2"
	table_name_3 = "tab3"
	dict_col_and_values_tab1 =  get_the_last_row(table_name_1, db_loc)
	dict_col_and_values_tab2 =  get_the_last_row(table_name_2, db_loc)
	print(dict_col_and_values_tab1)
	print(dict_col_and_values_tab2)
	del dict_col_and_values_tab1["ID"]
	del dict_col_and_values_tab2["ID"]
	del dict_col_and_values_tab1["MONTH"]
	del dict_col_and_values_tab2["MONTH"]

	compare= {}
	for col in dict_col_and_values_tab1.keys():
		if dict_col_and_values_tab1[col] >= dict_col_and_values_tab2[col]:
			compare[col] = False
		else:
			compare[col] = True 
	
	print("The dict used for creating data in tab3",compare)

	command = "DELETE FROM {} ".format(table_name_3)
	command += ";"
	executing_command(command, db_loc)

	command = create_insert_command(table_name_3, compare)
	executing_command(command, db_loc)

if __name__ == "__main__":
	run_compare()