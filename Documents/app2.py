from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

text =[]

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == 'POST':
        note=request.form["note"]
        text.append(note)
        return redirect(url_for('index'))
    return render_template("index.html", notes = text)
   
if __name__ == '__main__':
    app.run(debug=True,port = 5003)