from flask import *  
from flask_sqlalchemy import SQLAlchemy  
  
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.sqlite3'  
app.config['SECRET_KEY'] = "secret key"  
  
db = SQLAlchemy(app)  
  
class student(db.Model):  
   id = db.Column('student_id', db.Integer, primary_key = True)  
   name = db.Column(db.String(100))  
   rollno = db.Column(db.Float(50))  
   branch= db.Column(db.String(200))   
   college= db.Column(db.String(10))  
  
   def __init__(self, name, rollno, section,college):  
      self.name = name  
      self.rollno = rollno
      self.branch = branch 
      self.college = college 
 
@app.route('/')  
def list():  
   return render_template('list.html', students = students.query.all() )  
 
@app.route('/add', methods = ['GET', 'POST'])  
#def addstudent():  
   if request.method == 'POST':  
      if not request.form['name'] or not request.form['rollno'] or not request.form['branch']:  
         flash('Please enter all the fields', 'error')  
      else:  
         student = students(request.form['name'], request.form['rollno'],  
            request.form['branch'], request.form['college'])  
           
         db.session.add(student)  
         db.session.commit()  
         flash('Record was successfully added')  
         return redirect(url_for('list'))  
   return render_template('add.html')  
  
if __name__ == '__main__':  
   db.create_all()  
   app.run(debug = True) 