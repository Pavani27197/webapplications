from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/')
def msg():
	return "<h2> hello, This is python lab </h2>"
@app.route('/home') 
def home():
	return redirect(url_for('msg')) 

if __name__ =='__main__':  
    app.run(debug = True)  