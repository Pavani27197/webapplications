from flask import *
app=Flask(__name__)
@app.route('/<name>')  
def msg(name):  
	return "<h2>welcome"+" "+name+ "</h2>"
@app.route('/home')
def home():
	return redirect(url_for('msg',name="pavani")) 

if __name__ =='__main__':  
    app.run(debug = True)  