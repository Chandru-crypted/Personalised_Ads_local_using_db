import sqlite3

def run_getting_col(table_name):
	'''
	Getting the column names from the sql database in the given table name
	'''
	db_loc = r'C:\Users\chand\Documents\P\Projects\personalised_ads_with_flask\db\payment_db.db'
	table_name_1 = str(table_name)

	# Getting the last row from the db
	command = "SELECT * FROM {} ".format(table_name_1) 
	command += "ORDER BY ID "
	command += "DESC LIMIT 1 ;"
	conn = sqlite3.connect(db_loc)
	curser = conn.execute(command)
	names = [description[0] for description in curser.description]
	conn.close()
	return (names)

if __name__ == "__main__":
	run_getting_col("tab1")
