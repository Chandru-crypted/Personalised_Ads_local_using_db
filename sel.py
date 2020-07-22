import sqlite3
def checking_connection(db_loc):
	#establishing a connection 
	conn = sqlite3.connect(db_loc)
	conn.close()
	return (True)


def run_sel(table_name_1):
	db_loc = r'C:\Users\chand\Documents\P\Projects\personalised_ads_with_flask\db\payment_db.db'
	#table_name_1 = "tab1"
	command = "SELECT * FROM {} ".format(table_name_1)
	command += "ORDER BY ID DESC"
	command += ";"
	conn = sqlite3.connect(db_loc)
	curser = conn.execute(command)
	data_tuple = []
	for row in curser:
		data_tuple.append(row[1:])
	conn.close()
	
	return (data_tuple)

if __name__ == "__main__":
	run_sel()