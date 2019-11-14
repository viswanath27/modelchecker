from flask import Flask, render_template, request,flash,session
from forms import  PostForm, InputForm
from werkzeug import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '16e562d5ee25333ffd3e53f3c879a125'

@app.route('/')
def start():
    return render_template("info.html")


@app.route('/submit', methods=['POST','GET'])
def submit():
    result = []
    cmd = "rm -rf cmd_file code_file.smv"
    os.system(cmd)
    
    code = request.form['code']
    result.append(code)
    execute = request.form['execute']
    result.append(execute)
    #print (code)
    #print (execute)
    codde_file = open("code_file.smv","w") 
    codde_file.writelines(code) 
    codde_file.close()
    execute_file = open("cmd_file","w") 
    execute_file.writelines(execute) 
    execute_file.close()
    cmd = "./nuXmv -source cmd_file > output_file.txt"
    os.system(cmd)
    result_file = open("output_file.txt","r")
    data = result_file.read()
    result.append(data)
    print (data)
    #print("Files written")
    #return 'You entered: {}'.format(request.form['text'])
    return render_template("usb_power.html",result=result)
    #return result

@app.route('/usb_power',methods=['GET','POST'])
def usb_power():
	inputform = InputForm()
	#form = PostForm()
	if inputform.validate_on_submit():
		print ("Analyze button pressed")
		print(inputform.code.data)
		print (inputform.execution.data)

	#if form.submit():
	#	print (form.title.data)
	#	print (form.body.data)
	'''
	form = ReusableForm(request.form)
	if request.method == 'POST':
		text=request.form['code']
		print (text)
	if form.validate():
		print (text) 
	else:
		flash('All the form fields are required. ')
	text = request.form.get('textbox')
	print(text)
	'''
	#text = request.form.get('textbox')
	#print (text)
	return render_template("usb_power.html",inputform=inputform)


@app.route('/ac_power')
def ac_power():
	return render_template("ac_power.html")


@app.route('/battery_backup')
def battery_backup():
	return render_template("battery_backup.html")	


if __name__ == '__main__':
    app.run(debug=True)


