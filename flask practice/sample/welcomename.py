from flask import Flask
app=Flask(__name__)
@app.route('/welcome/<name>')  
def msg(name):  
    return "<h2>welcome"+" "+name+ "</h2>"
  
if __name__ =='__main__':  
    app.run(debug = True)  