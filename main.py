from flask import Flask,render_template

app = Flask("website")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/api/v1/<station>/<date>')
def api(station,date):
    temperature = 34
    data = {
        "station": station,
        "date": date,
        "temperature": temperature
    }
    return data

if __name__ == '__main__':
    app.run(debug=True)