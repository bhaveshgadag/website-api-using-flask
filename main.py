from flask import Flask,render_template

app = Flask("website")

@app.route("/")
def home():
    return render_template("index.html")


app.run(debug=True)