from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collegeinfo.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collegeinfo.db'
mydb = SQLAlchemy(app)

class Signup(mydb.Model):
	id = mydb.Column(mydb.Integer, primary_key = True)
	s_name = mydb.Column(mydb.String(200))
	roll_no = mydb.Column(mydb.String(50))
	mail_id = mydb.Column(mydb.String(200))
	phone_no= mydb.Column(mydb.String(50))
	s_branch= mydb.Column(mydb.String(100))

	def __init__(self, Name,Rollnumber,EmailId,PhoneNo,S_Branch):
		self.s_name= Name
		self.roll_no = Rollnumber
		self.mail_id = EmailId
		self.phone_no = PhoneNo
		self.s_branch = S_Branch
@app.route('/myportal/signup',methods=['POST','GET'])
def signup():
	if request.method == "POST":
		data=request.form
		stu_name = data['studentname']
		stu_rollno = data['rollno']
		stu_mailid = data['email']
		stu_phno = data['phoneno']
		stu_branch = data['branch']
		#print(data)
		#print(stu_name,stu_rollno,stu_mailid,stu_phno,stu_branch)
		sgn = Signup(stu_name,stu_rollno,stu_mailid,stu_phno,stu_branch)
		mydb.session.add(sgn)
		mydb.session.commit()
		return render_template('status.html')
	return render_template('signup.html')
@app.route('/myportal/studentlist')
def display():
	return render_template('showdetails.html',data=Signup.query.all())
if __name__ == '__main__':
	mydb.create_all()
	app.run(debug=True)