from flask import Flask, render_template
# here Flask is the class
#from forms import RegistrationForm
from flask import request, redirect
from Updater import run_updater

from sel import run_sel


app = Flask(__name__)
# telling the flask where to look for the static files and templates

#routes are what we type in browser to navigate in browser
# Like we have contact pages and about pages 
@app.route("/")
@app.route("/home")
def hello():
	posts = run_sel()
	return render_template("table.html", posts= posts) 

	#whatever variable that we pass here as an arrgument and also as the value is the same variable
	# it means we can acess that posts inside the template 
	# flask uses jinja template engine

@app.route("/about")
def about():
	return render_template("about.html", title = "About")


@app.route("/update", methods = ["GET" , "POST"])
def register():

	if request.method == "POST":
		req = request.form
		#username = req.get("username")

		input_dict = {}
		input_dict["DATE"] = str(req.get("date"))
		input_dict["FOOD"] = float(req.get("food"))
		input_dict["FUEL"] = float(req.get("fuel"))

		run_updater(input_dict)
		
		return render_template("updated.html", title = "Updated !", posts = input_dict)

	return render_template("update.html", title = "Update")

if __name__ == "__main__":
	app.run(debug = True)