from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def index():
    m = []
    if request.method=="POST":
        string = request.form['expression']
        match = request.form['find_string']
        com = re.compile(string)
        matching = com.search(match)
        m.append(matching)
        return render_template("index.html", m=m)
    return render_template("index.html")
    
if __name__=="__main__":
    app.run(debug=True,use_reloader = False)

