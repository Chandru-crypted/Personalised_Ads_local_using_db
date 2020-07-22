import sqlite3 

# Getting values from the tab3 
db_loc = r'C:\Users\chand\Documents\P\Projects\Locally_personalised_ads\db\payment_db.db'
table_name_3 = "tab3"

command = "SELECT * FROM {} ".format(table_name_3) 
conn = sqlite3.connect(db_loc)
curser = conn.execute(command)
names = [description[0] for description in curser.description]
values = []
dict = {}
for row in curser:
	values = list(row)
i = 0
for col in names :
	if (values[i]):
		dict[col] = values[i]
	i += 1 
conn.close()
print(dict)

print("\t \t \t \t \t Social media \t \t \t \t")

from random import seed
from random import randint


pos_of_ads = []
pos_of_ads.append(randint(1, 9))
pos_of_ads.append(randint(1, 9))


for j in range(10):
	if j in pos_of_ads:	
		print("\t \t \t \t ------------------------------------- \t \t \t \t ")
		for i in range(10):
			print("\t \t \t \t |                                     | \t \t \t \t")
			if i == 5:
				print(" \t \t \t \t Ads of {} \t \t \t ".format(list(dict.keys())))
		print("\t \t \t \t ------------------------------------- \t \t \t \t")

	print("\t \t \t \t ------------------------------------- \t \t \t \t ")
	for i in range(10):
		print("\t \t \t \t |                                     | \t \t \t \t")
	print("\t \t \t \t ------------------------------------- \t \t \t \t")