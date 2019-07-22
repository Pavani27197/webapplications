from flask import *
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.sqlite3'  
 
  
db = SQLAlchemy(app)  
  
class Sample(db.Model):  
   id = db.Column(db.Integer, primary_key = True)  
   Name = db.Column(db.String(100))  
   EmailId = db.Column(db.Float(50))  
   Rollnumber = db.Column(db.String(200))
   Collegename = db.Column(db.String(100))
   def __init__(self, Name, EmailId,Rollnumber,Collegename):  
      self.Name = Name  
      self.EmailId = EmailId  
      self.Rollnumber = Rollnumber
      self.Collegename = Collegename
@app.route('/mypage/show') 
def show():
	data.Sample.query.all()
	return render_template("show.html",data=data)   
@app.route('/mypage/register',methods=['POST','GET'])
def register():
	if request.method=="POST":
		Name = request.form['fname']
		EmailId = request.form['emailid']
		Rollnumber = request.form['rollnumber']
		Collegename = request.form['collegename']
		#print(Name,EmailId,PhoneNumber)
		flash("you are successfuly registered")  
		return render_template("log.html",n=Name,ei=EmailId,rn=Rollnumber,ca=Collegename)
		#sm=Sample(Name,EmailId,PhoneNumber,Collegename)
		#db.session.add(sm)
		#db.session.commit()
		#return "<h2>record stored</h2>"
	flash("you can register now") 
	return render_template("register.html")
@app.route('/mypage/login') 
def signin():	
	return render_template("login.html")

if __name__=='__main__':
	app.secret_key="my key"
	db.create_all()
	app.run(debug=True)
