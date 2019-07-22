from flask import Flask
app=Flask(__name__)
@app.route('/welcome/<name>/<int:rollnumber>/')  
def msg(name,rollnumber):  
    return "<h2>welcome"+" "+name+"<br>This is ur rollnumber :"+str(rollnumber)+"</br>" "</h2>"
  
if __name__ =='__main__':  
    app.run(debug = True)  