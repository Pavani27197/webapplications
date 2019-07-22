from flask import Flask
app=Flask(__name__)

@app.route('/home')
@app.route('/mymassage')
@app.route('/home/mypage')
def hello():
    return "<h1>hai hello iam python<h1>"

@app.route('/nomsg')
def mymassage():
    return "<h2>ni project</h2>"

if __name__=="__main__":
    app.run(debug=True)#app.debug=True
