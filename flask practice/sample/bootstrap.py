from flask import Flask,render_template
app = Flask(__name__)  
@app.route('/mypage/bootstrap')  
def bootstrap():  
    return render_template('bootstrap.html')  
if __name__ == '__main__':  
    app.run(debug = True)  