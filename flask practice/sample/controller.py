from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/home')   
def hello():  
    return "hello, this is flask";  
  
if __name__ =='__main__':  
    app.run(debug = True)  