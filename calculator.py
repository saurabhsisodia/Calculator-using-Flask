from flask import Flask,render_template,session,request
app=Flask(__name__)

@app.route('/')
def home():
	return render_template("calculator.html")

@app.route('/ans',methods=["POST","GET"])
def ans():
	if request.method=="POST":
		total=request.form["total"]
		if total!="":
			try:
				total=eval(total)
				return render_template("inherited_for_calculator.html",total=total)
			except:
				valid="Please enter correct expression"
				return render_template("inherited_for_calculator.html",valid=valid)

	return render_template("calculator.html")

if __name__=="__main__":
	app.run(debug=True)

