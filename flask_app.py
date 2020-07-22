import os
from flask import Flask, render_template
# here Flask is the class
#from forms import RegistrationForm
from flask import request, redirect
from Updater import run_updater

from sel import run_sel

from getting_col_names import run_getting_col 

	

app = Flask(__name__)

# telling the flask where to look for the static files and templates

#routes are what we type in browser to navigate in browser
# Like we have contact pages and about pages 
@app.route("/")
@app.route("/home")
def hello():
	columns_1 = run_getting_col("tab1")
	names_tab1 = columns_1[1:]	
	print(names_tab1)
	posts = []
	posts.append(names_tab1)
	posts.append(run_sel("tab1"))
	print(posts)
	return render_template("table.html", posts= posts) 

	#whatever variable that we pass here as an arrgument and also as the value is the same variable
	# it means we can acess that posts inside the template 
	# flask uses jinja template engine


@app.route("/update", methods = ["GET" , "POST"])
def register():

	columns_1 = run_getting_col("tab1")
	names_tab1= columns_1[2:]
	# names_tab2 = run_getting_col("tab2")
	# names_tab3 = run_getting_col("tab3")

	if request.method == "POST":
		req = request.form
		#username = req.get("username")

		input_dict = {}
		input_dict["DATE"] = str(req.get("DATE"))
		for cols in names_tab1:
			input_dict[str(cols)] = float(req.get(str(cols)))
		print(input_dict)

		run_updater(input_dict)

		# Dont worry about changing updater and compre cuz they are already dynamic 
		return render_template("updated.html", title = "Updated !", posts = input_dict)

	return render_template("update.html", title = "Update", posts = names_tab1)

@app.route("/ads", methods = ["GET", "POST"])
def ads():
	if request.method == "POST":
		req = request.form
		noofads = req.get("noof_ads")
		noofads = int(noofads)

		print(noofads)

		columns_3 = run_getting_col("tab3")
		columns_3 = columns_3[1:]
		data = run_sel("tab3")

		# data is a list of tuples but tab3 will have only one tuple so 
		dict_ads = {}
		i = 0
		for d in data[0]:
			dict_ads[columns_3[i]] = d
			i += 1
		print(dict_ads)

		s = 0
		for k in dict_ads.keys():
			s += dict_ads[k] 

		print(s)

		for k in dict_ads.keys():
			print(dict_ads[k])
			v = (dict_ads[k] / s)
			dict_ads[k] = v

		for k in dict_ads.keys():
			dict_ads[k] = int(dict_ads[k] * noofads)

		del_keys = []
		for k in dict_ads.keys():
			if dict_ads[k] == 0:
				del_keys.append(k)

		print(del_keys)
		print(dict_ads)


		for k in del_keys:
			del dict_ads[k]

		list_ads = list(dict_ads.items()) 
		list_ads = sorted(list_ads, key = lambda x: x[1], reverse = True)

		print(list_ads)
		
		return render_template("ads.html", title= "Ads", posts = list_ads)

	return render_template("sel_noofads.html", title = "Number of ads")

@app.route("/about")
def about():
	return render_template("about.html", title = "About")

if __name__ == "__main__":
	app.run(debug = True)


#<img src="../static/{{ a[0] }}/{{ i }}.jpg" alt="{{a[0] {i} }}" >